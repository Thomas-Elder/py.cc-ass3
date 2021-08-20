from os import replace
import re
import requests
import json

from .models import User, Athlete, Coach, Session

API_STRING = "https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/"
API_user = API_STRING + "user"
API_athlete = API_STRING + "athlete"
API_coach = API_STRING + "coach"
API_session = API_STRING + "session"

def get_user(id):
    """
    load_user
    Gets the user details from the API.
    """

    response = requests.get(API_user + f"?Email={id}")
    result = response.json()['result']
    
    if result is None:
        return None
    else:
        return User(result['Email'], result['Email'], result['Password'], result['Coach'])


def put_user(user: User):
    """
    put_user
    Puts the user details from the API.
    """
    json_user = {
        "Email": user.email,
        "Password": user.password,
        "Coach": user.coach
    }

    response = requests.put(API_user, json=json_user)
    return response

def check_email_unique(email: str) -> bool:
    """
    check_email_unique
    
    Returns true if the given email is not already in the database.
    """
    user = get_user(email)

    return user is None

def check_password(email: str, password: str) -> bool:
    """
    check_password

    Returns true if the password stored with the email matches.
    """
    user = get_user(email)
    
    if user is None:
        return False
    else:
        return user.password == password

def get_athlete(id: str):
    """
    get_athlete
    Gets the athlete details from the API for this id.
    """

    response = requests.get(API_athlete + f"?Email={id}")

    result = response.json()['result']['Item']

    if 'Coach' in result:
        coach = result['Coach']
    else:
        coach = None
    
    return Athlete(result['Email'], result['Name'], result['Age'], result['WeightClass'], coach=coach, sessions=result['Sessions'])

def get_athletes():
    """
    get_athletes
    Gets all athletes details from the API.
    """

    response = requests.get(API_athlete)

    results = response.json()['result']['Items']
    athletes = []
    for result in results:

        if 'Coach' in result:
            coach = result['Coach']
        else:
            coach = None
        
        athletes.append(Athlete(result['Email'], result['Name'], result['Age'], result['WeightClass'], coach=coach, sessions=result['Sessions']))

    return athletes


def put_athlete(athlete: Athlete):
    """
    put_athlete
    Puts the passed athlete to the API.
    """

    json_athlete = {
        "Email": athlete.email,
        "Name": athlete.name,
        "Age": athlete.age,
        "WeightClass": athlete.weightclass,
        "Coach": athlete.coach,
        "Sessions": athlete.sessions
    }

    response = requests.put(API_athlete, json=json_athlete)
    return response

def get_coach(id: str):
    """
    get_coach
    Gets the coach details from the API for this id.
    """
    response = requests.get(API_coach + f"?Email={id}")

    result = response.json()['result']['Item']

    return Coach(result['Email'], result['Name'], result['Athletes'])

def put_coach(coach: Coach):
    """
    put_coach
    Puts the passed coach to the API.
    """

    json_coach = {
        "Email": coach.email,
        "Name": coach.name,
        "Athletes": coach.athletes
    }

    requests.put(API_coach, json=json_coach)

def get_sessions():
    """
    get_sessions
    Gets all session details from the API.
    """

    response = requests.get(API_session)

    results = response.json()['result']

    #print(f'response.json() {response.json()}')

    sessions = []
    for result in results:
        
        sessions.append(Session(result['Key'], result['Date'], result['Exercises']))

    return sessions


def put_session(session: Session, email: str):
    """
    put_session
    Puts the passed session to the API.
    """

    json_session = {
        "Key": session.key,
        "Date": session.date,
        "Exercises": session.exercises
    }

    # Add session to Sessions table
    response = requests.put(API_session, json=json_session)

    athlete = get_athlete(email)
    athlete.sessions.append(session.key)

    json_athlete = {
        "Email": athlete.email,
        "Name": athlete.name,
        "Age": athlete.age,
        "WeightClass": athlete.weightclass,
        "Coach": athlete.coach,
        "Sessions": athlete.sessions
    }

    # Add session to this athlete 
    response = requests.put(API_athlete, json=json_athlete)
    
    return response