"""Feature entity."""
import warnings
from typing import Any, List

from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from butterfree.constants import DataType
from butterfree.transform.transformations import (
    AggregatedTransform,
    CustomTransform,
    SparkFunctionTransform,
    SQLExpressionTransform,
    StackTransform,
    TransformComponent,
)
from butterfree.transform.transformations.h3_transform import H3HashTransform


class Feature:
    """Defines a Feature.

    A Feature is the result of a transformation over one (or more) data columns
    over an input dataframe. Transformations can be as simple as renaming,
    casting types, mathematical expressions or complex functions/models.

    Attributes:
        name: feature name.
            Can be use by the transformation to derive multiple output columns.
        description: brief explanation regarding the feature.
        dtype: data type for the output columns of this feature.
        from_column: original column to build feature.
            Used when there is transformation or the transformation has no
            reference about the column to use for.
        transformation: transformation that will be applied to create this
            feature.

    """

    def __init__(
        self,
        name: str,
        description: str,
        dtype: DataType = None,
        from_column: str = None,
        transformation: TransformComponent = None,
    ) -> None:
        self.name = name
        self.description = description
        self.transformation = transformation
        self.dtype = dtype
        self.from_column = from_column

    @property
    def dtype(self) -> Any:
        """Attribute dtype getter."""
        return self.__dtype  # type: ignore

    @dtype.setter
    def dtype(self, value: DataType) -> None:
        if (
            not (
                isinstance(self.transformation, AggregatedTransform)
                or isinstance(self.transformation, SparkFunctionTransform)
            )
            and value is None
        ):
            raise ValueError(
                "dtype can't be None, except if the transformation is "
                "AggregatedTransform or SparkFunctionTransform"
            )

        if value is not None and not isinstance(value, DataType):
            raise ValueError("dtype must be a DataType.")

        self.__dtype = value

    @property
    def from_column(self) -> Any:
        """Attribute from_column getter."""
        return self.__from_column  # type: ignore

    @from_column.setter
    def from_column(self, value: str) -> None:
        if (
            isinstance(self.transformation, CustomTransform)
            or isinstance(self.transformation, SQLExpressionTransform)
            or isinstance(self.transformation, H3HashTransform)
            or isinstance(self.transformation, StackTransform)
        ) and value is not None:
            raise ValueError(
                f"from_column parameter doesn't need to be declared, "
                f"the column name {value} would be overwritten with "
                f"another name."
            )

        if value is not None and not isinstance(value, str):
            raise ValueError("from_column must be a string.")

        self.__from_column = value

    @property
    def transformation(self) -> Any:
        """Attribute transformation getter."""
        return self.__transformation

    @transformation.setter
    def transformation(self, value: TransformComponent) -> None:
        self.__transformation = value

        if value is not None:
            self.__transformation.parent = self

    def get_output_columns(self) -> List[str]:
        """Get output columns that will be generated by this feature engineering.

        Returns
            Output columns names.
        """
        if self.transformation is not None:
            return self.transformation.output_columns
        return [self.name]

    def transform(self, dataframe: DataFrame) -> DataFrame:
        """Performs a transformation to the feature pipeline.

        Args:
            dataframe: input dataframe for the transformation.

        Returns:
            Transformed dataframe.
        """
        if self.transformation:
            return self.transformation.transform(dataframe)

        if self.from_column:
            if self.name in dataframe.columns:
                warnings.warn(
                    f"The column name {self.name} "
                    "already exists in the dataframe and "
                    "will be overwritten with another column."
                )

            dataframe = dataframe.withColumn(self.name, col(self.from_column))

        if self.dtype:
            dataframe = dataframe.withColumn(
                self.name, col(self.name).cast(self.dtype.spark)
            )
        return dataframe
