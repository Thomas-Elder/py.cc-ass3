from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests
from flask_login import login_user, logout_user, login_required, current_user

bp = Blueprint('coach', __name__)

@login_required
@bp.route('/coach/athletes')
def athletes():

    return render_template('coach/athletes.html', current_user=current_user)

@login_required
@bp.route('/coach/sessions')
def sessions():

    return render_template('coach/sessions.html', current_user=current_user)