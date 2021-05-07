from typing import Callable

from awsglue.context import GlueContext

from easyglue.utils import reader_method


class JDBCMixin:
    glue_context: GlueContext
    connection_options_dict: dict
    connection_options: Callable

    @reader_method
    def jdbc(self, dbtable: str, url: str, user: str, password: str,
             redshift_tmp_dir: str = "", custom_jdbc_driver_s3_path: str = "", custom_jdbc_driver_class_name: str = "",
             database_type: str = "", transformation_ctx: str = "", push_down_predicate: str = ""):
        """
        Reads a dataset from a JDBC source by calling create_dynamic_frame.from_options with the right configuration
        :param self: Self reference to the EasyDynamicFrameReader class
        :param dbtable: Name of the JDBC database
        :param url: JDBC URL to connect to
        :param user: Username to authenticate with when connecting to the JDBC database
        :param password: Password to authenticate with when connecting to the JDBC database
        :param redshift_tmp_dir: Temporary path to be used when reading/writing from/to Redshift
        :param custom_jdbc_driver_s3_path: Path to the S3 object containing the custom JDBC driver to be used
        :param custom_jdbc_driver_class_name: Class name to be used when using a custom driver
        :param database_type: JDBC database type
        :param transformation_ctx: Glue transformation context
        :param push_down_predicate: Push down predicate to be applied
        :return: DynamicFrame representing the JDBC table
        """

        self.connection_options({
            'url': url,
            'dbtable': dbtable,
            'redshiftTmpDir': redshift_tmp_dir,
            'user': user,
            'password': password,
        })

        if custom_jdbc_driver_s3_path and custom_jdbc_driver_class_name:
            self.connection_options({
                'customJdbcDriverS3Path': custom_jdbc_driver_s3_path,
                'customJdbcDriverClassName': custom_jdbc_driver_class_name
            })

        db_type = database_type if database_type else url.split(':')[1]

        return self.glue_context.create_dynamic_frame.from_options(connection_type=db_type,
                                                                   connection_options=self.connection_options_dict,
                                                                   transformation_ctx=transformation_ctx,
                                                                   push_down_predicate=push_down_predicate)
