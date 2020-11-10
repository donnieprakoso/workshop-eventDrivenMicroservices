import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    try:                
        '''
        [TASK] Logs event variable to Amazon CloudWatch Logs. This way we know that Producer emitted a message and this function will consume that event.
        '''
    except Exception as e:
        logger.error(e)
