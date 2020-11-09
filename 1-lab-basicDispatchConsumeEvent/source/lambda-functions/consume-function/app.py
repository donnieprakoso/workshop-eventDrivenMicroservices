import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    try:                
        print(event)
    except Exception as e:
        logger.error(e)
