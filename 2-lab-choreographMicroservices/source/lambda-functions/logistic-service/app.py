import time
import boto3
import json
import os
from datetime import datetime 
'''
Lambda func for logistic service
'''


def save_to_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    response = table.update_item(
        Key={'ID': id},
        UpdateExpression="set time_logistic_service=:sts",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        })


def lambda_handler(event, context):
    print(event)
    print('logistic_service is called')
    data = event['detail']['data']
    save_to_db(data['ID'])
    response = {'status': 200}
    return response
