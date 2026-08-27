import json
import os
import boto3

sqs = boto3.client("sqs")
QUEUE_URL = os.environ.get("PROCESSING_QUEUE_URL")


def lambda_handler(event, context):
    if not QUEUE_URL:
        raise RuntimeError("PROCESSING_QUEUE_URL is not configured")

    messages = []
    for record in event.get("Records", []):
        s3 = record.get("s3", {})
        bucket = s3.get("bucket", {}).get("name")
        key = s3.get("object", {}).get("key")

        if not bucket or not key:
            continue

        payload = {
            "bucket": bucket,
            "key": key,
            "event_name": record.get("eventName"),
        }

        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(payload),
        )
        messages.append(response.get("MessageId"))

    return {
        "statusCode": 200,
        "queued": len(messages),
        "messageIds": messages,
    }
