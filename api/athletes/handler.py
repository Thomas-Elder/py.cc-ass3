import json

def create_athlete(event, context):
    body = {
        "message": "Creating athlete",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def read_athlete(event, context):
    body = {
        "message": "Reading athlete",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def update_athlete(event, context):
    body = {
        "message": "Updating athlete",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def delete_athlete(event, context):
    body = {
        "message": "Deleting athlete",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response