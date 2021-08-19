
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
from ..api import get_athlete, get_coach, get_athletes
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint('coach', __name__)

@login_required
@bp.route('/coach/athletes')
def athletes():
    
    all_athletes = get_athletes()
    #coach_athlete_emails = get_coach(current_user.id).athletes
    coach = get_coach(current_user.id)
    coach_athletes = filter(lambda athlete: athlete.email in coach.athletes, all_athletes)
    #for email in coach_athlete_emails:
    #    coach_athletes.append(get_athlete(email))

    
    

    return render_template('coach/athletes.html', current_user=current_user, all_athletes=all_athletes,coach_athletes=coach_athletes)

@login_required
@bp.route('/coach/sessions')
def sessions():

    return render_template('coach/sessions.html', current_user=current_user)