import time
import boto3
import json
import os
from datetime import datetime
import logging

'''
Lambda func for fulfilment service
'''
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def save_to_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    table.update_item(
        Key={'ID': id},
        UpdateExpression="set time_fulfilment_service=:sts",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        })


def lambda_handler(event, context):
    logger.info(event)
    logger.info('fulfilment_service is called')
    client = boto3.client('events')
    data = {}
    data['metadata'] = event['detail']['metadata']
    data['data'] = event['detail']['data']
    response = client.put_events(Entries=[
        {
            'Source': 'fulfilment_service',
            'DetailType': 'fulfilment_completed',
            'Detail': json.dumps(data),
            'EventBusName': os.getenv("EVENTBUS_NAME")
        },
    ])
    save_to_db(data['data']['ID'])
    response = {'status': 200}
    return response
