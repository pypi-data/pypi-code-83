from modules.torch.models.assetType import AssetType
from modules.torch.models.create_asset import RelationType, CreateAssetRelation
from modules.torch.models.datasource import DataSource, DatasourceSourceType


class AssetRelation:

    def __init__(self,
                 fromAssetId: str,
                 toAssetId: str,
                 currentSnapshot: str,
                 snapshots,
                 id: int,
                 isDeleted: bool,
                 relation: RelationType,
                 metadata=None):
        """
            Description:
                Asset relation class
        :param fromAssetId: source asset id
        :param toAssetId: sink asset id
        :param currentSnapshot: current version of the asset relation
        :param snapshots: version list
        :param id: asset relation id
        :param isDeleted: isDeleted or not in newer version
        :param relation: (RelationType) relation type
        :param metadata: (List[AssetMetadata]) metadata of the asset relation
        """
        self.fromAssetId = fromAssetId
        self.toAssetId = toAssetId
        self.currentSnapshot = currentSnapshot
        self.snapshots = snapshots
        self.id = id
        self.isDeleted = isDeleted
        self.relation = relation
        self.metadata = metadata

    def __eq__(self, other):
        return self.toAssetId == other.toAssetUUID and self.fromAssetId == other.fromAssetUUID

    def __repr__(self):
        return f"SnapshotData({self.__dict__})"


class Asset:

    def __init__(self,
                 alias=None,
                 assembly=None,
                 assetType: AssetType = None,
                 createdAt=None,
                 currentSnapshot=None,
                 description=None,
                 id=None,
                 isCustom=None,
                 isDeleted=None,
                 name=None,
                 parentId=None,
                 snapshots=None,
                 sourceType=None,
                 uid=None,
                 updatedAt=None,
                 client=None
                 ):
        """
            Description:
                Asset class
        :param alias: alias of the asset
        :param assembly: (Datasource) data source details
        :param assetType: type of the asset
        :param createdAt: creation time of the asset
        :param currentSnapshot: current version of the asset
        :param description: desc of the asset
        :param id: asset id
        :param isCustom: is custom asset or not
        :param isDeleted: is deleted or not in current version of the datasource
        :param name: name of the asset
        :param parentId: parent id of the asset
        :param snapshots: version list
        :param sourceType: source type of the asset's datasource
        :param uid: uid of the asset
        :param updatedAt: updated time of the asset
        """
        self.alias = alias
        self.createdAt = createdAt
        self.currentSnapshot = currentSnapshot
        self.description = description
        self.id = id
        self.isCustom = isCustom
        self.isDeleted = isDeleted
        self.name = name
        self.parentId = parentId
        self.snapshots = snapshots
        self.uid = uid
        self.updatedAt = updatedAt
        if isinstance(assembly, dict):
            self.datasource = DataSource(**assembly)
        else:
            self.datasource = assembly
        if isinstance(assetType, dict):
            self.assetType = AssetType(**assetType)
        else:
            self.assetType = assetType
        if isinstance(sourceType, dict):
            self.sourceType = DatasourceSourceType(**sourceType)
        else:
            self.sourceType = sourceType

        # self.datasource = assembly
        # self.sourceType = sourceType

        self.client = client

    def __repr__(self):
        return f"Asset({self.__dict__})"

    # convert asset relation to dict type
    def _convert_asset_relation_to_dict(self, asset_relation: CreateAssetRelation):
        """
        Description:
            Convert CreateAssetRelation class instance to dict type
        :param assetRelation: CreateAssetRelation class instance
        :return: dict form of CreateAssetRelation class instance
        """
        payload = asset_relation.__dict__
        payload['relationType'] = asset_relation.relationType.name
        asset_relation_payload = {'data': payload}
        return asset_relation_payload

    # create relation between asset
    def create_asset_relation(self, to_asset_uuid: str, relation_type: RelationType,
                              snapshots=None):
        """
        Description:
            used to create relation between any 2 existing assets
        :param snapshots:
        :param relation_type:
        :param to_asset_uuid:
        :return: created AssetRelation class instance
        """
        if snapshots is None:
            snapshots = [self.currentSnapshot]
        asset_relation = CreateAssetRelation(
            fromAssetUUID=self.uid,
            assemblyId=self.datasource.id,
            toAssetUUID=to_asset_uuid,
            relationType=relation_type,
            currentSnapshot=self.currentSnapshot,
            snapshots=snapshots
        )
        payload = self._convert_asset_relation_to_dict(asset_relation)
        return self.client.create_asset_relation(payload)
