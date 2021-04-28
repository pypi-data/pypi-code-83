from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Hashable, Any, Dict, Type
from rfb_mc.runner_random import RunnerRandom
from rfb_mc.types import Params

RestrictiveFormulaParams = TypeVar("RestrictiveFormulaParams", bound=Hashable)
# parameter that determines all formula generation related values

RestrictiveFormulaProperties = TypeVar("RestrictiveFormulaProperties")
# properties of the restrictive formula that are determined by the parameters

RestrictiveFormulaInstanceParams = TypeVar("RestrictiveFormulaInstanceParams")


# values that parameterize a specific instance generated by the module and will be used by
# the runner implementations to reconstruct the formula in the format of which ever solver is used


class RestrictiveFormulaModuleBase(
    Generic[RestrictiveFormulaParams, RestrictiveFormulaProperties, RestrictiveFormulaInstanceParams],
    ABC,
):
    @classmethod
    @abstractmethod
    def get_guid(cls) -> str:
        """
        UID of the restrictive formula module that needs to be deterministic and
        unique across all other restrictive formula module implementations.

        An abbreviation of the name that is unlikely to be reused is suggested and possibly a
        version number in order to differentiate between different generations of the same module.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def encode_restrictive_formula_params(
        cls,
        params: Params,
    ) -> Any:
        """
        Encodes the formula parameters into a native python type.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def decode_restrictive_formula_params(
        cls,
        params: Any,
    ) -> Params:
        """
        Decodes the formula parameters from the native python type generated by the encoder.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get_restrictive_formula_properties(
        cls,
        params: Params,
        restrictive_formula_params: RestrictiveFormulaParams,
    ) -> RestrictiveFormulaProperties:
        """
        Returns properties that the restrictive formula generation posses with the given parameters.
        """

        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def generate_restrictive_formula_instance_params(
        cls,
        params: Params,
        restrictive_formula_params: RestrictiveFormulaParams,
        q: int,
        random: RunnerRandom,
    ) -> RestrictiveFormulaInstanceParams:
        """
        Generate the restrictive formula instance params for the given params using randomness from the random runner
        class.
        """

        raise NotImplementedError()


restrictive_formula_module_map: Dict[str, Type[RestrictiveFormulaModuleBase]] = {}
"""
Map from restrictive formula module uid to module class.
"""


def register_restrictive_formula_module(rfm: Type[RestrictiveFormulaModuleBase]):
    restrictive_formula_module_map[rfm.get_guid()] = rfm


def get_restrictive_formula_module(uid: str) -> Type[RestrictiveFormulaModuleBase]:
    if uid in restrictive_formula_module_map:
        return restrictive_formula_module_map[uid]
    else:
        raise RuntimeError(f"Restrictive formula module \"{uid}\" is required but is not registered")