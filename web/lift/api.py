from os import replace
import re
import requests

from .models import User

API_STRING = "https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/"
API_athlete = API_STRING + "athlete"
API_coach = API_STRING + "coach/"

def load_user(id):
    """
    load_user
    Gets the user details from the API, for use by flask_login for tracking current_user.
    """

    response = requests.get(API_athlete + f"?Email={id}")
    
    if response.status_code is 200:
        athlete = response.json()['result']
        user = User(athlete['Email'], athlete['Email'], "", athlete['Name'], athlete['WeightClass'], athlete['Sessions'], coach=False)
    else:
        response = requests.get(API_coach + f"?Email={id}")

        if response.status_code is 200:
            coach = response.json()['result']
            user = User(coach['Email'], coach['Email'], "", coach['Name'], coach['WeightClass'], coach['Sessions'], coach=True)

    return user

def get_athlete(id: str=None):
    """
    get_athlete
    Gets the athlete details from the API for this id.
    """

    if id is None:
        response = requests.get(API_athlete)

        if response.status_code is 200:
            users = []

            for athlete in response.json()['result']:
                users.append(User(athlete['Email'], athlete['Email'], "", athlete['Name'], athlete['WeightClass'], athlete['Sessions'], coach=False))

            return response.json()['result']

    else:
        response = requests.get(API_athlete + f"?Email={id}")
        print(response.json()['result'])

        if response.status_code is 200:
            athlete = response.json()['result']['Item']
            user = User(athlete['Email'], athlete['Email'], "", athlete['Name'], athlete['WeightClass'], athlete['Sessions'], coach=False)

            return user


def put_athlete(athlete: User):
    """
    put_athlete
    Puts the passed athlete to the API.
    """
    # JSON User object
    requests.put(API_athlete, athlete)

def get_coach(id: str):
    """
    get_coach
    Gets the coach details from the API for this id.
    """
    if id is None:
        response = requests.get(API_coach)

        if response.status_code is 200:
            users = []

            for coach in response.json()['result']:
                users.append(User(coach['Email'], coach['Email'], "", coach['Name'], coach['WeightClass'], coach['Sessions'], coach=True))

            return response.json()['result']

    else:
        response = requests.get(API_coach + f"?Email={id}")
        print(response.json()['result'])

        if response.status_code is 200:
            coach = response.json()['result']['Item']
            user = User(coach['Email'], coach['Email'], "", coach['Name'], coach['WeightClass'], coach['Sessions'], coach=True)

            return user

def put_coach(coach: User):
    """
    put_coach
    Puts the passed coach to the API.
    """
    # JSON User object
    requests.put("https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/athlete/", coach)