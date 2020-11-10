def handler(event, context):
    if event['address']:
        event['humanReviewRequired']=False
    else:
        event['humanReviewRequired']=True
    return event
