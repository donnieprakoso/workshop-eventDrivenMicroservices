import time
import boto3
import json
import os
from datetime import datetime
import logging

'''
Lambda func for invoice service
'''
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def save_to_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    table.update_item(
        Key={'ID': id},
        UpdateExpression="set time_invoice_service=:sts",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        })

def lambda_handler(event, context):
    logger.info(event)
    logger.info('invoice_service is called')
    data = event['detail']['data'] 
    save_to_db(data['ID'])
    response = {'status':200}
    return response
