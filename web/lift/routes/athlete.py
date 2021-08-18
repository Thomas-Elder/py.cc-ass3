from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
from flask_login import login_user, logout_user, login_required, current_user

import requests

bp = Blueprint('athlete', __name__)

#
# Exercise routes
#
@login_required
@bp.route('/athlete/exercise/history')
def exercise_history():

    return render_template('athlete/exercise/history.html', current_user=current_user)

#
# Session routes
#
@login_required
@bp.route('/athlete/session/history')
def session_history():

    return render_template('athlete/session/history.html', current_user=current_user)

@login_required
@bp.route('/athlete/session/new')
def session_new():

    return render_template('athlete/session/new.html', current_user=current_user)