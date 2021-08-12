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

@app.route('/coach/put', methods=['PUT'])
def put_coach(event=None, context=None):
    
    details = request.json

    # Build coach object
    coach = {
        "Email": details['Email'],
        "Name": details['Name'],
        "Age": details['Age'],
        "WeightClass": details['WeightClass'],
    }

    body = {
        "message": "Creating coach",
        "coach": coach,
        "input": event,
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach/get', methods=['GET'])
def get_coach(event=None, context=None):
    
    if 'id' in request.args:

        body = {
            "message": "Reading coach",
            "id": request.args.get('id'),
            "input": event,
        }

    else:

        body = {
            "message": "No id, reading all coachs",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach/patch', methods=['PATCH'])
def patch_coach(event=None, context=None):
    
    details = request.json

    # Build coach object
    coach = {
        "Email": details['Email'],
        "Name": details['Name'],
        "Age": details['Age'],
        "WeightClass": details['WeightClass'],
    }

    body = {
        "message": "Updating coach",
        "coach": coach,
        "input": event,
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/coach/delete', methods=['DELETE'])
def delete_coach(event=None, context=None):
    
    if 'id' in request.args:

        body = {
            "message": f"Deleting coach: {request.args.get('id')}",
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