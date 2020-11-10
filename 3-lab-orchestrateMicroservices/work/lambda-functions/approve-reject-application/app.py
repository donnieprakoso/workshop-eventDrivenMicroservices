def handler(event, context):
    amount = event[0]['amount']
    data = event[0]
    if amount <= 1000:
        data['reviewApproved'] = True
    elif amount <= 5000:
        data['reviewApproved'] = True
    else:
        data['reviewApproved'] = False
    return data 
