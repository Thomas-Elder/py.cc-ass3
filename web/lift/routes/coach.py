from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests

bp = Blueprint('coach', __name__)

@bp.route('/coach/athletes')
def athletes():

    return render_template('coach/athletes.html')

@bp.route('/coach/sessions')
def sessions():

    return render_template('coach/sessions.html')