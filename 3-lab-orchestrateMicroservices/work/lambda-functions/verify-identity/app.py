def handler(event, context):
    if event['document']:
        event['humanReviewRequired']=False
    else:
        event['humanReviewRequired']=True
    return event
