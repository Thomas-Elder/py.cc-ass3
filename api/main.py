
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

# Athlete
@app.route('/athlete', methods=['PUT'])
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

@app.route('/athlete', methods=['GET'])
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

@app.route('/athlete', methods=['PATCH'])
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

@app.route('/athlete', methods=['DELETE'])
def delete_athlete(event=None, context=None):
    
    if 'Email' in request.args:

        body = {
            "message": f"Deleting athlete: {request.args.get('Email')}",
            "input": event
        }

    else:

        body = {
            "message": "No Email, cannot delete",
            "input": event,
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# Session routes
@app.route('/session', methods=['PUT'])
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

@app.route('/session', methods=['GET'])
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

@app.route('/session', methods=['PATCH'])
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

@app.route('/session', methods=['DELETE'])
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

# Coach routes
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