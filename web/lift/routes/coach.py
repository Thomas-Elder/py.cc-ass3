from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests

bp = Blueprint('coach', __name__)

@bp.route('/coach/athletes')
def history():

    return render_template('coach/athletes.html')

@bp.route('/coach/sessions')
def new():

    return render_template('coach/sessions.html')