from ..api import get_athlete, get_sessions, put_session
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime

from .forms import SessionForm
from ..models import Session

import requests

bp = Blueprint('athlete', __name__)

#
# Exercise routes
# Not implemented
#
@login_required
@bp.route('/athlete/exercise/history')
def exercise_history():

    return render_template('athlete/exercise/history.html', current_user=current_user)

#
# Session routes
#
@login_required
@bp.route('/athlete/session', methods=['GET', 'POST'])
def sessions():

    athlete = get_athlete(current_user.id)
    all_sessions = get_sessions()
    athlete_sessions = filter(lambda session: session.key in athlete.sessions, all_sessions)

    return render_template('athlete/sessions.html', athlete_sessions=athlete_sessions, current_user=current_user)

@login_required
@bp.route('/athlete/session/add', methods=['GET', 'POST'])
def session_add():

    form = SessionForm()

    if form.date.data is not None:

        exercises = []

        for exercise in form.exercises.data:
            if exercise['variation'] != "":
                exercises.append({
                    "Name": exercise['variation'],
                    "Repetitions": exercise['repetitions'],
                    "Sets": exercise['sets'],
                    "Weight": exercise['weight']
                })

        key = datetime.now().strftime("%c")
        session = Session(key, request.form['date'], exercises)
        put_session(session, current_user.id)

        return redirect(url_for('athlete.sessions'))
    else:
        return render_template('athlete/sessions_add.html', current_user=current_user, form=form)