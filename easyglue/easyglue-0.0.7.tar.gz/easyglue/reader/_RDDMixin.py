from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

from easyglue.utils import reader_method


class RDDMixin:
    glue_context: GlueContext

    @reader_method
    def rdd(self, source_rdd, name: str, schema=None, sample_ratio=None) -> DynamicFrame:
        """
        Reads a dataset from an RDD object
        :param self: Self reference to the EasyDynamicFrameReader class
        :param source_rdd: RDD object to read from
        :param name: Name to be given to the resulting DynamicFrame
        :param schema: (Optional) Schema to be applied to the resulting DynamicFrame
        :param sample_ratio: (Optional) Sampling ratio to apply when reading from the RDD
        :return: DynamicFrame object representing the RDD
        """
        return self.glue_context.create_dynamic_frame_from_rdd(data=source_rdd,
                                                               name=name,
                                                               schema=schema,
                                                               sample_ratio=sample_ratio)
