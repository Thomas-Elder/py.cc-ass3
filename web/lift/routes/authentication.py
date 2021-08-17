
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_login import login_user, logout_user, login_required, current_user

# import forms

API = "https://4oodow0413.execute-api.us-east-1.amazonaws.com/dev/"

bp = Blueprint('authentication', __name__, url_prefix='/authentication')

@bp.route('/register', methods=('GET', 'POST'))
def register():

    form = {}

    if request.method == 'POST':

        if form.validate_on_submit():
            
            # send to api with new athlete/coach object
            # if user is athlete:
            # request.post(API /athlete, user) - in JSON format
            # else:
            # request.post(API /coach, user) - in JSON format

            return redirect(url_for('authentication.login'))

        else:
            return render_template('authentication/register.html', current_user=current_user, form=form)

    else:
        return render_template('authentication/register.html', current_user=current_user, form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():

    form = {}

    if request.method == 'POST':

        if form.validate_on_submit():

            # get user from API with this email, pass to login_user
            # login_user(get_user(form.email.data))
            return redirect(url_for('subscription.music'))

        else:
            return render_template('authentication/login.html', current_user=current_user, form=form)   

    else:
        return render_template('authentication/login.html', current_user=current_user, form=form)   

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))