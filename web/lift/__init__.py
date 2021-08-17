import os

from flask import Flask

def create_application(test_config=None):
    # create and configure the application
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_mapping(SECRET_KEY='dev')

    from .routes import index, session, exercise
    application.register_blueprint(index.bp)  
    application.register_blueprint(session.bp)
    application.register_blueprint(exercise.bp)

    return application