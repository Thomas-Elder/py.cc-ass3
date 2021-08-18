from os import replace
import re
import requests
import json

from .models import User, Athlete, Coach

API_STRING = "https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/"
API_user = API_STRING + "user"
API_athlete = API_STRING + "athlete"
API_coach = API_STRING + "coach"

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

    result = response.json()['result']
    return Athlete(result['Email'], result['Email'], result['Name'], result['Age'], result['WeightClass'], result['Sessions'])


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

    result = response.json()['result']
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

    requests.put(API_coach, json_coach)