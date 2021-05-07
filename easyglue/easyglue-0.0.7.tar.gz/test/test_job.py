from pyspark.context import SparkContext
from awsglue.context import GlueContext

import easyglue


def main():
    # Create a Glue context
    glue = GlueContext(SparkContext.getOrCreate())

    # Create a DynamicFrame using the 'persons_json' table
    persons_dyf = glue.read().json("s3://bertolb/sampledata/mockaroo/json")
    # persons_dyf = glue.read().catalog("legislators", "persons_json")
    # persons_dyf = glueContext.create_dynamic_frame.from_catalog(database="legislators", table_name="persons_json")

    # Print out information about this data
    print("Count:  ", persons_dyf.count())
    persons_dyf.printSchema()


if __name__ == "__main__":
    main()
