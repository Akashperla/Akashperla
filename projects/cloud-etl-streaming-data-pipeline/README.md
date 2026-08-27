# Cloud ETL & Streaming Data Pipeline

A portfolio implementation of the resume project focused on distributed ETL, AWS event-driven processing, and resilient data workflows.

## Tech Stack

Python, PySpark, Apache Spark, AWS S3, AWS Lambda, Amazon SQS, Amazon RDS

## Architecture

1. Raw files land in an S3 input location.
2. An S3 event invokes the Lambda handler.
3. Lambda publishes a processing message to SQS.
4. The PySpark ETL job reads raw data, validates required fields, removes duplicates, standardizes timestamps, and writes curated Parquet output.
5. Curated data can be loaded into RDS or consumed by downstream analytics services.

## Project Structure

```text
cloud-etl-streaming-data-pipeline/
├── README.md
├── etl_job.py
├── lambda_handler.py
└── requirements.txt
```

## Run the ETL Job

```bash
spark-submit etl_job.py \
  --input s3://your-bucket/raw/ \
  --output s3://your-bucket/curated/
```

## Lambda Environment Variables

- `PROCESSING_QUEUE_URL` - SQS queue URL used for event-driven processing.

## Key Engineering Features

- Distributed transformations with Spark/PySpark.
- Schema validation and malformed-record filtering.
- Duplicate removal and timestamp normalization.
- S3-based ingestion and curated data output.
- Lambda + SQS decoupling for event-driven workflows.
- Error handling suitable for retry/DLQ integration.

This repository is a portfolio implementation intended to demonstrate the architecture and technologies described in the project section of my resume.
