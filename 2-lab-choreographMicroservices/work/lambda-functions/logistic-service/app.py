import time
import boto3
import json
import os
from datetime import datetime 
import logging

'''
Lambda func for logistic service
'''
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def save_to_db(id):
    '''
    [ADDITIONAL TASK] Save the data into database ONLY by passing the ID
    Create a field called time_logistic_service and passing the current timestamp with format "MONTH-DAY-YEAR HOUR:MINUTES:SECONDS"
    '''


def lambda_handler(event, context):
    '''
    [ADDITIONAL TASK] Parse ID from event message sent by Amazon EventBridge and call save_to_db function to save into DynamoDB
    '''
