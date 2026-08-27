import argparse
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

SCHEMA = StructType([
    StructField("record_id", StringType(), False),
    StructField("source", StringType(), True),
    StructField("event_time", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amount", DoubleType(), True),
])


def build_spark() -> SparkSession:
    return SparkSession.builder.appName("cloud-etl-streaming-data-pipeline").getOrCreate()


def transform(df):
    return (
        df.filter(F.col("record_id").isNotNull())
          .dropDuplicates(["record_id"])
          .withColumn("source", F.coalesce(F.col("source"), F.lit("unknown")))
          .withColumn("category", F.lower(F.trim(F.col("category"))))
          .withColumn("event_timestamp", F.to_timestamp("event_time"))
          .drop("event_time")
    )


def main(input_path: str, output_path: str):
    spark = build_spark()
    raw = spark.read.option("header", True).schema(SCHEMA).csv(input_path)
    curated = transform(raw)

    curated.write.mode("overwrite").partitionBy("category").parquet(output_path)

    print(f"Input rows: {raw.count()}")
    print(f"Curated rows: {curated.count()}")
    print(f"Output written to: {output_path}")
    spark.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="S3 or local input path")
    parser.add_argument("--output", required=True, help="S3 or local output path")
    args = parser.parse_args()
    main(args.input, args.output)
