from dataclasses import dataclass, asdict
from typing import List
from modules.torch.models.snapshot import SnapshotData, AssociatedItemType
from modules.torch.models.create_asset import CreateAsset, CreateAssetRelation, RelationType, AssetMetadata


@dataclass
class ConfigProperty:
    key: str = None
    value: str = None


@dataclass
class SourceType:
    id: int = None
    name: str = None


class CreateDataSource:

    def __init__(self,
                 name: str,
                 sourceType: SourceType,
                 description: str = None,
                 isVirtual: bool = None,
                 connectionId: int = None,
                 configProperties: List[ConfigProperty] = []
                 ):
        self.name = name
        self.description = description
        self.sourceType = SourceType(sourceType.id, sourceType.name)
        if isVirtual is None and connectionId is None:
            raise Exception('Either provide connection configuration for the assembly or enable isVirtual flag')
        if isVirtual is None:
            self.connectionId = connectionId
            self.configProperties = configProperties
            self.isVirtual = False
        if connectionId is None:
            self.isVirtual = isVirtual

    def __eq__(self, other):
        return self.name == other.name and self.connectionId == other.connectionId

    def __repr__(self):
        return f"DataSource({self.name!r})"


@dataclass
class DatasourceSourceModel:
    id: int = None
    name: str = None


@dataclass
class DatasourceSourceType:

    def __init__(self, id, name, sourceModel=None, connectionTypeId=None):
        """
            Description:
                Datasource source type
        :param id: id of the source type
        :param name: name of the source type
        :param sourceModel: source model
        :param connectionTypeId: (int) connection type id for the given source type
        """
        self.id = id
        self.name = name
        self.connectionTypeId = connectionTypeId
        if isinstance(sourceModel, dict):
            self.sourceModel = DatasourceSourceModel(**sourceModel)
        else:
            self.sourceModel = sourceModel

    def __repr__(self):
        return f"DatasourceSourceType({self.__dict__})"


class DataSource:

    def __init__(self,
                 name: str,
                 isSecured: bool,
                 isVirtual: bool,
                 id: int,
                 createdAt: str = None,
                 updatedAt: str = None,
                 assemblyProperties=None,
                 conn=None,
                 connectionId: int = None,
                 crawler: object = None,
                 currentSnapshot: str = None,
                 description: str = None,
                 sourceType: DatasourceSourceModel = None,
                 securityConfig=None,
                 schedule=None,
                 configuration=None,
                 client=None,
                 **kwargs
                 ):
        """
            Description:
                datasource class.
        :param name: name of the datasource
        :param isSecured: is secured or not
        :param isVirtual: is virtual datasource or not
        :param id: id of the datasource
        :param createdAt: creation time of the datasource
        :param updatedAt: updated time of the datasource
        :param assemblyProperties: datasource properties
        :param conn: connection details for the ds
        :param connectionId: connection id of the datasource
        :param crawler: crawler details of the datasource
        :param currentSnapshot: current version of the datasource
        :param description: desc of the datasource
        :param sourceType: (DatasourceSourceModel) source type details
        :param securityConfig: security configuration for the given ds
        :param schedule: scheduled exp
        :param configuration: configurations
        """
        self.name = name
        self.isSecured = isSecured
        self.isVirtual = isVirtual
        self.id = id
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.assemblyProperties = assemblyProperties
        self.conn = conn
        self.connectionId = connectionId
        self.crawler = crawler
        self.currentSnapshot = currentSnapshot
        self.description = description
        self.securityConfig = securityConfig
        self.schedule = schedule
        self.configuration = configuration
        if isinstance(sourceType, dict):
            self.sourceType = DatasourceSourceType(**sourceType)
        else:
            self.sourceType = sourceType

        self.client = client

    def __repr__(self):
        return f"DataSource({self.__dict__})"

    # convert asset to dict type
    def _convert_asset_to_dict(self, asset: CreateAsset):
        """
            Description:
                Convert CreateAsset class instance to dict type
            :param asset: CreateAsset class instance
            :return: dict form of CreateAsset class instance
        """
        payload = asset.__dict__
        metadata = []
        for md in asset.metadata:
            metadata.append(asdict(md))
        payload['metadata'] = metadata
        asset_payload = {'data': payload}
        return asset_payload

    # to create an asset
    def create_asset(self, name: str, uid: str, asset_type_id: int, parent_id: int = None, description: str = None,
                     snapshots=None, metadata: List[AssetMetadata] = None):
        """
        Description:
            used to create asset in datasource
        :return: asset created
        """
        if snapshots is None:
            snapshots = [self.currentSnapshot]
        asset = CreateAsset(
            name=name,
            description=description,
            assemblyId=self.id,
            uid=uid,
            assetTypeId=asset_type_id,
            sourceTypeId=self.sourceType.id,
            isCustom=False,
            parentId=parent_id,
            currentSnapshot=self.currentSnapshot,
            snapshots=snapshots,
            metadata=metadata
        )
        payload = self._convert_asset_to_dict(asset)
        return self.client.create_asset(payload)

    # convert snapshot data to dict type
    def _convert_snapshot_data_to_dict(self, snapshot_data: SnapshotData):
        """
            Description:
                Convert SnapshotData class instance to dict type
            :param snapshotData: SnapshotData class instance
            :return: dict form of SnapshotData class instance
        """
        payload = snapshot_data.__dict__
        payload['associatedItemType'] = snapshot_data.associatedItemType.name
        snaoshot_payload = {'data': payload}
        return snaoshot_payload

    # initialise new version of snapshot for a datasource
    def initialise_snapshot(self, uid: str):
        """
        Description:
            Used to initialise new version of snapshot for a datasource
        :param uid: uid of new snapshot version
        :return: created snapshotData class instance
        """
        if uid is None:
            raise Exception('uid for new snapshot version is required')
        snapshot_data = SnapshotData(
            uuid=uid,
            associatedItemType=AssociatedItemType.ASSEMBLY,
            associatedItemId=self.id
        )

        payload = self._convert_snapshot_data_to_dict(snapshot_data)
        snapshot = self.client.initialise_snapshot(payload)
        self.currentSnapshot = snapshot.uuid
        return snapshot

    # get current version of datasource
    def get_current_snapshot(self):
        """
        Description:
            If you want to get current version of a datasource
        :return: SnapshotData class instance of datasource
        """
        snapshot = self.client.get_current_snapshot(self.id)
        if self.currentSnapshot is None:
            self.currentSnapshot = snapshot.uuid
        return snapshot

    def get_asset(self, uid: str = None, id: int = None):
        """"
            Description:
                Find an asset of the datasource
            :param uid: (String) uid of the asset
            :param id: (Int) id of the asset in torch catalog
        """
        if uid is None and id is None:
            raise Exception('Either provide uid or id to find an asset')
        if uid is not None:
            return self.client.get_asset_by_uid(uid=uid)
        if id is not None:
            return self.client.get_asset_by_id(id=id)