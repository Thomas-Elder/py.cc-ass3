
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
from ..api import get_athlete, get_coach
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint('coach', __name__)

@login_required
@bp.route('/coach/athletes')
def athletes():

    athlete_emails = get_coach(current_user.id).athletes

    athletes = []

    for email in athlete_emails:
        athletes.append(get_athlete(email))

    return render_template('coach/athletes.html', current_user=current_user, athletes=athletes)

@login_required
@bp.route('/coach/sessions')
def sessions():

    return render_template('coach/sessions.html', current_user=current_user)