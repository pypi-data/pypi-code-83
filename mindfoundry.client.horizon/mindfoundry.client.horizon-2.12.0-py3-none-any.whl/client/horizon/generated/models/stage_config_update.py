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
from ..models.stationarisation_stage_config import StationarisationStageConfig
from ..models.trading_simulation_stage_config import TradingSimulationStageConfig
from ..models.trading_specification_stage_config import TradingSpecificationStageConfig

T = TypeVar("T", bound="StageConfigUpdate")


@attr.s(auto_attribs=True)
class StageConfigUpdate:
    """  """

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
    ]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.config, ProblemSpecificationConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, StationarisationStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, FeatureGenerationStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, FilterStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, RefinementStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, BacktestStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, PredictionStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, TradingSpecificationStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, TradingSimulationStageConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, ClassificationSpecificationConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, ClassificationDiscoveryConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, ClassificationBacktestConfig):
            config = self.config.to_dict()

        elif isinstance(self.config, LstmBacktestStageConfig):
            config = self.config.to_dict()

        else:
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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
        ]:
            try:
                config_type0: ProblemSpecificationConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type0 = ProblemSpecificationConfig.from_dict(data)

                return config_type0
            except:  # noqa: E722
                pass
            try:
                config_type1: StationarisationStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type1 = StationarisationStageConfig.from_dict(data)

                return config_type1
            except:  # noqa: E722
                pass
            try:
                config_type2: FeatureGenerationStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type2 = FeatureGenerationStageConfig.from_dict(data)

                return config_type2
            except:  # noqa: E722
                pass
            try:
                config_type3: FilterStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type3 = FilterStageConfig.from_dict(data)

                return config_type3
            except:  # noqa: E722
                pass
            try:
                config_type4: RefinementStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type4 = RefinementStageConfig.from_dict(data)

                return config_type4
            except:  # noqa: E722
                pass
            try:
                config_type5: BacktestStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type5 = BacktestStageConfig.from_dict(data)

                return config_type5
            except:  # noqa: E722
                pass
            try:
                config_type6: PredictionStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type6 = PredictionStageConfig.from_dict(data)

                return config_type6
            except:  # noqa: E722
                pass
            try:
                config_type7: TradingSpecificationStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type7 = TradingSpecificationStageConfig.from_dict(data)

                return config_type7
            except:  # noqa: E722
                pass
            try:
                config_type8: TradingSimulationStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type8 = TradingSimulationStageConfig.from_dict(data)

                return config_type8
            except:  # noqa: E722
                pass
            try:
                config_type9: ClassificationSpecificationConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type9 = ClassificationSpecificationConfig.from_dict(data)

                return config_type9
            except:  # noqa: E722
                pass
            try:
                config_type10: ClassificationDiscoveryConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type10 = ClassificationDiscoveryConfig.from_dict(data)

                return config_type10
            except:  # noqa: E722
                pass
            try:
                config_type11: ClassificationBacktestConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type11 = ClassificationBacktestConfig.from_dict(data)

                return config_type11
            except:  # noqa: E722
                pass
            try:
                config_type12: LstmBacktestStageConfig
                if not isinstance(data, dict):
                    raise TypeError()
                config_type12 = LstmBacktestStageConfig.from_dict(data)

                return config_type12
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type13: LstmPredictionStageConfig
            config_type13 = LstmPredictionStageConfig.from_dict(data)

            return config_type13

        config = _parse_config(d.pop("config"))

        stage_config_update = cls(
            config=config,
        )

        stage_config_update.additional_properties = d
        return stage_config_update

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
