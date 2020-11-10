import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    try:                
        client = boto3.client('events')
        payload = {"title":"This is a test message","test":True}
        client.put_events(
            Entries=[
                {
                    'Source': 'lab1-bdc-dispatch',
                    'DetailType': 'message-received',
                    'Detail': json.dumps(payload),
                    'EventBusName': os.getenv("EVENT_BUS_NAME")
                },
            ]
        )
        logger.info("Message dispatched")
        return "Message dispatched"
    except Exception as e:
        logger.error(e)
