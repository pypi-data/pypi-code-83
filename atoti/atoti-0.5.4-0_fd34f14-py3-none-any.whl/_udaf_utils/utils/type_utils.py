from typing import Any, Collection, Mapping

from ...type import DOUBLE_ARRAY, DataType

# Gives acceptable input types for ``JavaFunctions`` depending on the type requested in the function's signature
TYPE_CONSTRAINTS: Mapping[str, Collection[str]] = {
    "double": ["double", "float", "long", "int"],
    "float": ["float", "long", "int"],
    "long": ["long", "int"],
    "int": ["int"],
    "double[]": ["double[]"],
    "float[]": ["float[]"],
    "long[]": ["long[]"],
    "int[]": ["int[]"],
    "object": ["object"],
}

# Currently supported types for Python constants.
PYTHON_TYPE_TO_JAVA_TYPE = {
    "str": "string",
    # Use the widest type to avoid compilation problems
    "int": "long",
    "float": "double",
}

ARRAY_TYPE_PREFIXES = (
    "double[]",
    "float[]",
    "int[]",
    "long[]",
    "atoti_list_double",
    "atoti_numpy_double",
    "atoti_list_float",
    "atoti_numpy_float",
    "atoti_list_int",
    "atoti_numpy_int",
    "atoti_list_long",
    "atoti_numpy_long",
)


def get_java_type(type_string: str) -> DataType:
    if type_string == "IVector":
        return DOUBLE_ARRAY

    return DataType(type_string.lower(), True)


def is_numeric_type(data_type: DataType) -> bool:
    """Checks if the data type is numeric."""
    return data_type.java_type in ["double", "float", "int", "long"]


def is_numeric_array_type(data_type: DataType) -> bool:
    """Checks if the data type is an array of numeric values."""
    return data_type.java_type.startswith(ARRAY_TYPE_PREFIXES)


def is_boolean_type(data_type: DataType) -> bool:
    """Checks if the data type is a boolean."""
    return data_type.java_type == "boolean"


def convert_python_type_to_java(value: Any):
    python_type = type(value).__name__
    java_type = PYTHON_TYPE_TO_JAVA_TYPE[python_type]
    if java_type is None:
        raise TypeError("Unsupported type: " + python_type)
    if python_type == "list":
        if not is_numeric_type(
            DataType(PYTHON_TYPE_TO_JAVA_TYPE[type(value[0]).__name__], True)
        ):
            raise TypeError("Only lists of numeric values are supported.")
    return DataType(java_type, True)


def simplify_java_type(java_type: str) -> str:
    """Simplifies custom atoti array types or returns the passed value"""
    if java_type.startswith(ARRAY_TYPE_PREFIXES):
        if "double" in java_type:
            return "double[]"
        if "float" in java_type:
            return "float[]"
        if "long" in java_type:
            return "long[]"
        if "int" in java_type:
            return "int[]"
    return java_type
