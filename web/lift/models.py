
from re import A
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, email, password, coach):
        self.id = id
        self.email = email
        self.password = password
        self.coach = coach

class Athlete():

    def __init__(self, email, name, age, weightclass, coach=None, sessions=[]):
        self.email = email
        self.name = name
        self.age = age
        self.weightclass = weightclass

        self.coach = coach
        self.sessions = sessions

class Coach():

    def __init__(self, email, name, athletes=[]):
        self.email = email
        self.name = name
        
        self.athletes = athletes
    