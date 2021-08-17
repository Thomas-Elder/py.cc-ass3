from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests
from ..api import get_athlete, get_coach

bp = Blueprint('', __name__)

@bp.route('/')
@bp.route('/index')
def index():

    message = get_athlete("test@gmail.com").email
    return render_template('index.html', message=message)