
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
from ..api import get_athlete, get_coach, get_athletes, put_coach, put_athlete
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint('coach', __name__)

@login_required
@bp.route('/coach/athletes', methods=['GET'])
def athletes():

    all_athletes = get_athletes()
    coach = get_coach(current_user.id)

    coach_athletes = filter(lambda athlete: athlete.email in coach.athletes, all_athletes)
    coachless_athletes = filter(lambda athlete: athlete.coach is None, all_athletes)

    return render_template('coach/athletes.html', current_user=current_user, coachless_athletes=coachless_athletes, coach_athletes=coach_athletes)

@login_required
@bp.route('/coach/athletes/add', methods=['POST'])
def athletes_add():

    coach = get_coach(current_user.id)
    coach.athletes.append(request.form['Email'])

    athlete = get_athlete(request.form['Email'])
    athlete.coach = coach.email

    put_athlete(athlete)
    put_coach(coach)

    return redirect(url_for('coach.athletes'))

#
# Not implemented
#
@login_required
@bp.route('/coach/sessions', methods=['GET'])
def sessions():

    return render_template('coach/sessions.html', current_user=current_user)