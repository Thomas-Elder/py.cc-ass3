
"""
This is a copy paste of the lambda functions
"""


import json, boto3
import re
from flask import Flask, request
app = Flask(__name__)

"""
Athlete resource
"""
@app.route('/', methods=['GET'])
def index(event=None, context=None):
    body = {
        "message": "Welcome to Lift API",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# Athlete
@app.route('/athlete', methods=['PUT'])
def put_athlete(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build athlete object
    athlete = {
        "Email": details["Email"],
        "Name": details["Name"],
        "Age": details["Age"],
        "Coach": details["Coach"],
        "WeightClass": details["WeightClass"],
        "Sessions": details["Sessions"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Athletes')
    response = table.put_item(
       Item=athlete
    )

    body = {
        "message": "Putting athlete",
        "result": athlete,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/athlete', methods=['GET'])
def get_athlete(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Athletes')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        email = event['queryStringParameters']['Email']

        athlete = table.get_item(Key={'Email': email})

        body = {
            "message": "Reading athlete",
            "result": athlete,
            "input": event,
        }

    else:

        response = table.scan()
        athletes = response['Items']

        body = {
            "message": "No Email, reading all athletes",
            "result": athletes,
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/athlete', methods=['PATCH'])
def patch_athlete(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build athlete object
    athlete = {
        "Email": details["Email"],
        "Name": details["Name"],
        "Age": details["Age"],
        "WeightClass": details["WeightClass"],
        "Sessions": details["Sessions"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Athletes')
    response = table.put_item(
       Item=athlete
    )

    body = {
        "message": "Updating athlete",
        "result": athlete,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/athlete', methods=['DELETE'])
def delete_athlete(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Athletes')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        email = event['queryStringParameters']['Email']

        athlete = table.delete_item(Key={'Email': email})

        body = {
            "message": "Deleting athlete",
            "result": athlete,
            "input": event,
        }

    else:

        body = {
            "message": "No Email, cannot delete record",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# Session routes
@app.route('/session', methods=['PUT'])
def put_session(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build session object
    session = {
        "Key": details["Key"],
        "Date": details["Date"],
        "Exercises": details["Exercises"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Sessions')
    response = table.put_item(
       Item=session
    )

    body = {
        "message": "Putting session",
        "result": session,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/session', methods=['GET'])
def get_session(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Sessions')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        key = event['queryStringParameters']['Key']

        session = table.get_item(Key={'Key': key})

        body = {
            "message": "Reading session",
            "result": session,
            "input": event,
        }

    else:

        response = table.scan()
        sessions = response['Items']

        body = {
            "message": "No Key, reading all sessions",
            "result": sessions,
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/session', methods=['PATCH'])
def patch_session(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build session object
    session = {
        "Key": details["Key"],
        "Date": details["Date"],
        "Exercises": details["Exercises"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Sessions')
    response = table.put_item(
       Item=session
    )

    body = {
        "message": "Patching session",
        "result": session,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/session', methods=['DELETE'])
def delete_session(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Sessions')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        key = event['queryStringParameters']['Key']

        session = table.delete_item(Key={'Key': key})

        body = {
            "message": "Deleting session",
            "result": session,
            "input": event,
        }

    else:

        body = {
            "message": "No Key, cannot delete record",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# Coach routes
@app.route('/coach', methods=['PUT'])
def put_coach(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build coach object
    coach = {
        "Email": details["Email"],
        "Name": details["Name"],
        "Athletes": details["Athletes"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Coaches')
    response = table.put_item(
       Item=coach
    )

    body = {
        "message": "Putting coach",
        "result": coach,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['GET'])
def get_coach(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Coaches')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        email = event['queryStringParameters']['Email']

        coach = table.get_item(Key={'Email': email})

        body = {
            "message": "Reading coach",
            "result": coach,
            "input": event,
        }

    else:

        response = table.scan()
        coaches = response['Items']

        body = {
            "message": "No Email, reading all coaches",
            "result": coaches,
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['PATCH'])
def patch_coach(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build athlete object
    coach = {
        "Email": details["Email"],
        "Name": details["Name"],
        "Sessions": details["Sessions"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Coaches')
    response = table.put_item(
       Item=coach
    )

    body = {
        "message": "Patching coach",
        "result": coach,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['DELETE'])
def delete_coach(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Coaches')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        email = event['queryStringParameters']['Email']

        coach = table.delete_item(Key={'Email': email})

        body = {
            "message": "Deleting coach",
            "result": coach,
            "input": event,
        }

    else:

        body = {
            "message": "No Email, cannot delete record",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# User routes
@app.route('/user', methods=['PUT'])
def put_user(event=None, context=None):
    
    details = json.loads(event['body'])
    
    # Build athlete object
    user = {
        "Email": details["Email"],
        "Password": details["Password"],
        "Coach": details["Coach"]
    }

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Users')
    response = table.put_item(
       Item=user
    )

    body = {
        "message": "Putting user",
        "result": user,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/user', methods=['GET'])
def lambda_handler(event=None, context=None):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')

    queryStringParameters = event['queryStringParameters']

    if queryStringParameters is not None:

        email = event['queryStringParameters']['Email']

        try: 
            user = table.get_item(Key={'Email': email})['Item']

        except:
            user = None

        body = {
            "message": "Reading user",
            "result": user,
            "input": event,
        }

    else:

        body = {
            "message": "No Email, can't read user"
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

#
# For local hosting
#
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=True)