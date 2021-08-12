import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(event=None, context=None):
    body = {
        "message": "Welcome to Lift API",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['PUT'])
def put_coach(event=None, context=None):
    
    details = request.json

    # Build coach object
    coach = {
        "Email": details['Email'],
        "Name": details['Name']
    }

    body = {
        "message": "Creating coach",
        "coach": coach,
        "input": event,
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['GET'])
def get_coach(event=None, context=None):
    
    if 'Email' in request.args:

        body = {
            "message": "Reading coach",
            "Email": request.args.get('Email'),
            "input": event,
        }

    else:

        body = {
            "message": "No Email, reading all coachs",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['PATCH'])
def patch_coach(event=None, context=None):
    
    details = request.json

    # Build coach object
    coach = {
        "Email": details['Email'],
        "Name": details['Name']
    }

    body = {
        "message": "Updating coach",
        "coach": coach,
        "input": event,
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach', methods=['DELETE'])
def delete_coach(event=None, context=None):
    
    if 'Email' in request.args:

        body = {
            "message": f"Deleting coach: {request.args.get('Email')}",
            "input": event
        }

    else:

        body = {
            "message": "No Email, cannot delete",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

#
# For local hosting
#
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=True)