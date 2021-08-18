import os

from flask import Flask
from flask_login import login_manager, login_user, logout_user, login_required, current_user, LoginManager
from .api import get_user

def create_application(test_config=None):
    # create and configure the application
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_mapping(SECRET_KEY='dev')

    from .routes import index
    from .routes import athlete, coach, authentication
    application.register_blueprint(index.bp)  
    application.register_blueprint(athlete.bp)
    application.register_blueprint(coach.bp)
    application.register_blueprint(authentication.bp)

    loginManager = LoginManager(application)
    @loginManager.user_loader
    def load_user(id):
        return get_user(id)

    return application