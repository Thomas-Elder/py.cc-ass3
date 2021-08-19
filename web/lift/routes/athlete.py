from web.lift.api import put_session
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
from flask_login import login_user, logout_user, login_required, current_user

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
@bp.route('/athlete/session')
def sessions():
    form = SessionForm()
    if form.validate_on_submit():
        session = Session()
        put_session(session, current_user.id)

        return render_template('athlete/sessions.html', current_user=current_user, form=form)
    else:
        return render_template('athlete/sessions.html', current_user=current_user, form=form)

@login_required
@bp.route('/athlete/session/add', methods=['POST'])
def session_add():

    return redirect(url_for('athlete.session'))