from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.backtest_stage_config import BacktestStageConfig
from ..models.classification_backtest_config import ClassificationBacktestConfig
from ..models.classification_discovery_config import ClassificationDiscoveryConfig
from ..models.classification_specification_config import ClassificationSpecificationConfig
from ..models.feature_generation_stage_config import FeatureGenerationStageConfig
from ..models.filter_stage_config import FilterStageConfig
from ..models.lstm_backtest_stage_config import LstmBacktestStageConfig
from ..models.lstm_prediction_stage_config import LstmPredictionStageConfig
from ..models.prediction_stage_config import PredictionStageConfig
from ..models.problem_specification_config import ProblemSpecificationConfig
from ..models.refinement_stage_config import RefinementStageConfig
from ..models.stage_type import StageType
from ..models.stationarisation_stage_config import StationarisationStageConfig
from ..models.trading_simulation_stage_config import TradingSimulationStageConfig
from ..models.trading_specification_stage_config import TradingSpecificationStageConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="StageSpecification")


@attr.s(auto_attribs=True)
class StageSpecification:
    """  """

    stage_type: StageType
    config: Union[
        BacktestStageConfig,
        ClassificationBacktestConfig,
        ClassificationDiscoveryConfig,
        ClassificationSpecificationConfig,
        FeatureGenerationStageConfig,
        FilterStageConfig,
        LstmBacktestStageConfig,
        LstmPredictionStageConfig,
        PredictionStageConfig,
        ProblemSpecificationConfig,
        RefinementStageConfig,
        StationarisationStageConfig,
        TradingSimulationStageConfig,
        TradingSpecificationStageConfig,
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stage_type = self.stage_type.value

        config: Union[Dict[str, Any], Unset]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ProblemSpecificationConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, StationarisationStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, FeatureGenerationStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, FilterStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, RefinementStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, BacktestStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, PredictionStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, TradingSpecificationStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, TradingSimulationStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, ClassificationSpecificationConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, ClassificationDiscoveryConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, ClassificationBacktestConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        elif isinstance(self.config, LstmBacktestStageConfig):
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        else:
            config = UNSET
            if not isinstance(self.config, Unset):
                config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stageType": stage_type,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stage_type = StageType(d.pop("stageType"))

        def _parse_config(
            data: object,
        ) -> Union[
            BacktestStageConfig,
            ClassificationBacktestConfig,
            ClassificationDiscoveryConfig,
            ClassificationSpecificationConfig,
            FeatureGenerationStageConfig,
            FilterStageConfig,
            LstmBacktestStageConfig,
            LstmPredictionStageConfig,
            PredictionStageConfig,
            ProblemSpecificationConfig,
            RefinementStageConfig,
            StationarisationStageConfig,
            TradingSimulationStageConfig,
            TradingSpecificationStageConfig,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                config_type0: Union[Unset, ProblemSpecificationConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type0 = UNSET
                _config_type0 = data
                if not isinstance(_config_type0, Unset):
                    config_type0 = ProblemSpecificationConfig.from_dict(_config_type0)

                return config_type0
            except:  # noqa: E722
                pass
            try:
                config_type1: Union[Unset, StationarisationStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type1 = UNSET
                _config_type1 = data
                if not isinstance(_config_type1, Unset):
                    config_type1 = StationarisationStageConfig.from_dict(_config_type1)

                return config_type1
            except:  # noqa: E722
                pass
            try:
                config_type2: Union[Unset, FeatureGenerationStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type2 = UNSET
                _config_type2 = data
                if not isinstance(_config_type2, Unset):
                    config_type2 = FeatureGenerationStageConfig.from_dict(_config_type2)

                return config_type2
            except:  # noqa: E722
                pass
            try:
                config_type3: Union[Unset, FilterStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type3 = UNSET
                _config_type3 = data
                if not isinstance(_config_type3, Unset):
                    config_type3 = FilterStageConfig.from_dict(_config_type3)

                return config_type3
            except:  # noqa: E722
                pass
            try:
                config_type4: Union[Unset, RefinementStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type4 = UNSET
                _config_type4 = data
                if not isinstance(_config_type4, Unset):
                    config_type4 = RefinementStageConfig.from_dict(_config_type4)

                return config_type4
            except:  # noqa: E722
                pass
            try:
                config_type5: Union[Unset, BacktestStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type5 = UNSET
                _config_type5 = data
                if not isinstance(_config_type5, Unset):
                    config_type5 = BacktestStageConfig.from_dict(_config_type5)

                return config_type5
            except:  # noqa: E722
                pass
            try:
                config_type6: Union[Unset, PredictionStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type6 = UNSET
                _config_type6 = data
                if not isinstance(_config_type6, Unset):
                    config_type6 = PredictionStageConfig.from_dict(_config_type6)

                return config_type6
            except:  # noqa: E722
                pass
            try:
                config_type7: Union[Unset, TradingSpecificationStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type7 = UNSET
                _config_type7 = data
                if not isinstance(_config_type7, Unset):
                    config_type7 = TradingSpecificationStageConfig.from_dict(_config_type7)

                return config_type7
            except:  # noqa: E722
                pass
            try:
                config_type8: Union[Unset, TradingSimulationStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type8 = UNSET
                _config_type8 = data
                if not isinstance(_config_type8, Unset):
                    config_type8 = TradingSimulationStageConfig.from_dict(_config_type8)

                return config_type8
            except:  # noqa: E722
                pass
            try:
                config_type9: Union[Unset, ClassificationSpecificationConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type9 = UNSET
                _config_type9 = data
                if not isinstance(_config_type9, Unset):
                    config_type9 = ClassificationSpecificationConfig.from_dict(_config_type9)

                return config_type9
            except:  # noqa: E722
                pass
            try:
                config_type10: Union[Unset, ClassificationDiscoveryConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type10 = UNSET
                _config_type10 = data
                if not isinstance(_config_type10, Unset):
                    config_type10 = ClassificationDiscoveryConfig.from_dict(_config_type10)

                return config_type10
            except:  # noqa: E722
                pass
            try:
                config_type11: Union[Unset, ClassificationBacktestConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type11 = UNSET
                _config_type11 = data
                if not isinstance(_config_type11, Unset):
                    config_type11 = ClassificationBacktestConfig.from_dict(_config_type11)

                return config_type11
            except:  # noqa: E722
                pass
            try:
                config_type12: Union[Unset, LstmBacktestStageConfig]
                if not isinstance(data, dict):
                    raise TypeError()
                config_type12 = UNSET
                _config_type12 = data
                if not isinstance(_config_type12, Unset):
                    config_type12 = LstmBacktestStageConfig.from_dict(_config_type12)

                return config_type12
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type13: Union[Unset, LstmPredictionStageConfig]
            config_type13 = UNSET
            _config_type13 = data
            if not isinstance(_config_type13, Unset):
                config_type13 = LstmPredictionStageConfig.from_dict(_config_type13)

            return config_type13

        config = _parse_config(d.pop("config", UNSET))

        stage_specification = cls(
            stage_type=stage_type,
            config=config,
        )

        stage_specification.additional_properties = d
        return stage_specification

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
