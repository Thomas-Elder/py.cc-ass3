import re
import requests

from .models import User

def load_user(id):

    response = requests.get(f"https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/athlete/email={id}")
    
    if response.status_code is 200:
        user = User(id, "", "", [], coach=False)
    else:
        response = requests.get(f"https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/coach/email={id}")

        if response.status_code is 200:
            user = User(id, "", "", [], coach=True)

    return user
