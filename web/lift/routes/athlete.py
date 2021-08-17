from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests

bp = Blueprint('athlete', __name__)

#
# Exercise routes
#
@bp.route('/athlete/exercise/history')
def exercise_history():

    return render_template('athlete/exercise/history.html')

#
# Session routes
#
@bp.route('/athlete/session/history')
def session_history():

    return render_template('athlete/session/history.html')

@bp.route('/athlete/session/new')
def session_new():

    return render_template('athlete/session/new.html')