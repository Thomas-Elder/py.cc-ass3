
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_login import login_user, logout_user, login_required, current_user

from ..models import Athlete, Coach, User
from ..api import put_athlete, put_coach, put_user, get_user
from .forms import RegisterAthleteForm, RegisterCoachForm, LoginForm

bp = Blueprint('authentication', __name__, url_prefix='/authentication')

@bp.route('/register/athlete', methods=('GET', 'POST'))
def register_athlete():

    form = RegisterAthleteForm()

    if request.method == 'POST':

        if form.validate_on_submit():

            put_athlete(Athlete(form.email.data, form.name.data, form.age.data, form.weightclass.data, []))
            put_user(User(form.email.data, form.email.data, form.password.data, False))

            return redirect(url_for('authentication.login'))

        else:
            return render_template('authentication/register_athlete.html', current_user=current_user, form=form)

    else:
        return render_template('authentication/register_athlete.html', current_user=current_user, form=form)

@bp.route('/register/coach', methods=('GET', 'POST'))
def register_coach():

    form = RegisterCoachForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            put_coach(Coach(form.email.data, form.name.data))
            put_user(User(form.email.data, form.email.data, form.password.data, True))

            return redirect(url_for('authentication.login'))

        else:
            return render_template('authentication/register_coach.html', current_user=current_user, form=form)

    else:
        return render_template('authentication/register_coach.html', current_user=current_user, form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            login_user(get_user(form.email.data))

            return redirect(url_for('index'))

        else:
            return render_template('authentication/login.html', current_user=current_user, form=form)   

    else:
        return render_template('authentication/login.html', current_user=current_user, form=form)   

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))