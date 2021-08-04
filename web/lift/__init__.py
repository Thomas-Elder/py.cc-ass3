import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    from .routes import index, session, exercise
    app.register_blueprint(index.bp)  
    app.register_blueprint(session.bp)
    app.register_blueprint(exercise.bp)

    return app