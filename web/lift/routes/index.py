from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests

bp = Blueprint('', __name__)

@bp.route('/')
@bp.route('/index')
def index():

    response = requests.get("https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/athlete")
    message = response.json()['message']

    return render_template('index.html', message=message)