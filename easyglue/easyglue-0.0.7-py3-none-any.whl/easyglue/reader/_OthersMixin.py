from typing import Any

from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import reader_method


class OthersMixin:
    glue_context: GlueContext
    connection_options_dict: dict

    @reader_method
    def dynamodb(self, table_name: str, transformation_ctx: str = "", **kwargs: Any) -> DynamicFrame:
        """
        Reads a DynamoDB dataset by calling create_dynamic_frame_from_options with the right configuration
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return:DynamicFrame representing the dataset
        """
        self.connection_options_dict['dynamodb.input.tableName'] = table_name

        return self.glue_context.create_dynamic_frame_from_options(connection_type='dynamodb',
                                                                   connection_options=self.connection_options_dict,
                                                                   transformation_ctx=transformation_ctx,
                                                                   kwargs=kwargs
                                                                   )

    @reader_method
    def ddb(self, table_name: str, transformation_ctx: str = "", **kwargs: Any) -> DynamicFrame:
        """
        Reads a DynamoDB dataset by calling create_dynamic_frame_from_options with the right configuration
        :param table_name: Name of the DynamoDB table
        :param transformation_ctx: Glue transformation context
        :param kwargs: Keyword arguments
        :return:DynamicFrame representing the dataset
        """
        return self.dynamodb(table_name, transformation_ctx, kwargs=kwargs)
