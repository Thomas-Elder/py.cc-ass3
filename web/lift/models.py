
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, email, name, weightclass, password, sessions, coach=False):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.weightclass = weightclass
        self.sessions = sessions
        self.coach = coach
