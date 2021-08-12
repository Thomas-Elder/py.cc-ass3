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

@app.route('/session/put', methods=['PUT'])
def put_session(event=None, context=None):
    
    details = request.json

    # Build session object
    session = {
        "Id": details['Id'],
        "Date": details['Date'],
        "Exercises": details['Exercises']
    }

    body = {
        "message": "Creating session",
        "session": session,
        "input": event
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/session/get', methods=['GET'])
def get_session(event=None, context=None):
    
    if 'id' in request.args:

        body = {
            "message": "Reading session",
            "id": request.args.get('id'),
            "input": event
        }

    else:

        body = {
            "message": "No id, reading all sessions",
            "input": event
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/session/patch', methods=['PATCH'])
def patch_session(event=None, context=None):
    
    details = request.json

    # Build session object
    session = {
        "Id": details['Id'],
        "Date": details['Date'],
        "Exercises": details['Exercises']
    }

    body = {
        "message": "Updating session",
        "session": session,
        "input": event
    }

    # Update DB

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

@app.route('/session/delete', methods=['DELETE'])
def delete_session(event=None, context=None):
    
    if 'id' in request.args:

        body = {
            "message": f"Deleting session: {request.args.get('id')}",
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