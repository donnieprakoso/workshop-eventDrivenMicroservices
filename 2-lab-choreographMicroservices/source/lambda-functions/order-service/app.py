import boto3
import os
import json
import uuid
from datetime import datetime 
'''
Lambda func for order service
'''


def save_to_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    response = table.update_item(
        Key={'ID': id},
        UpdateExpression="set time_order_service=:sts",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        })


def lambda_handler(event, context):
    print(event)
    try:
        id = str(uuid.uuid4())
        data = {}
        data['metadata'] = {"service": "demo-eventbridge"}
        data['data'] = {}
        data['data']['ID'] = id
        data['data']['order'] = {
            'total': 100,
            'currency': 'SGD',
            'billing_address': 'Address 12345, Singapore'
        }
        data['data']['line_items'] = []
        ex_item = {
            'sku': '12345',
            'item_name': 'Item name testing',
            'quantity': 1
        }
        data['data']['line_items'].append(ex_item)
        ex_item = {
            'sku': '23456',
            'item_name': 'Item name testing',
            'quantity': 1
        }
        data['data']['line_items'].append(ex_item)
        client = boto3.client('events')
        response = client.put_events(Entries=[
            {
                'Source': 'order_service',
                'DetailType': 'order_created',
                'Detail': json.dumps(data),
                'EventBusName': os.getenv("EVENTBUS_NAME")
            },
        ])
        print(response)
        save_to_db(id)
        response = {'statusCode': 200, 'body': json.dumps("{}")}
        return response
    except Exception as e:
        print(e)
        response = {'statusCode': 500, 'body': json.dumps("{}")}
        return response
