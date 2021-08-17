
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_login import login_user, logout_user, login_required, current_user

# import forms

bp = Blueprint('authentication', __name__, url_prefix='/authentication')

@bp.route('/register', methods=('GET', 'POST'))
def register():

    form = {}

    if request.method == 'POST':

        if form.validate_on_submit():
            
            # send to api with new athlete/coach object
            
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