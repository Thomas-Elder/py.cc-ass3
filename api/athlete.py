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

@app.route('/athlete/put', methods=['PUT'])
def put_athlete(event=None, context=None):
    
    details = request.json

    # Build athlete object
    athlete = {
        "Email": details['Email'],
        "Name": details['Name'],
        "Age": details['Age'],
        "WeightClass": details['WeightClass'],
    }

    body = {
        "message": "Creating athlete",
        "athlete": athlete,
        "input": event,
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/athlete/get', methods=['GET'])
def get_athlete(event=None, context=None):
    
    if 'Email' in request.args:

        body = {
            "message": "Reading athlete",
            "Email": request.args.get('Email'),
            "input": event,
        }

    else:

        body = {
            "message": "No Email, reading all athletes",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/athlete/patch', methods=['PATCH'])
def patch_athlete(event=None, context=None):
    
    details = request.json

    # Build athlete object
    athlete = {
        "Email": details['Email'],
        "Name": details['Name'],
        "Age": details['Age'],
        "WeightClass": details['WeightClass'],
    }

    body = {
        "message": "Updating athlete",
        "athlete": athlete,
        "input": event,
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/athlete/delete', methods=['DELETE'])
def delete_athlete(event=None, context=None):
    
    if 'id' in request.args:

        body = {
            "message": f"Deleting athlete: {request.args.get('id')}",
            "input": event
        }

    else:

        body = {
            "message": "No id, cannot delete",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

#
# For local hosting
#
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8181, debug=True)