from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests
from ..api import get_athlete, get_coach, put_user, get_user
from flask_login import current_user

from ..models import User

bp = Blueprint('', __name__)

@bp.route('/')
@bp.route('/index')
def index():

    return render_template('index.html', current_user=current_user)