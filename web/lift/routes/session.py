from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests

bp = Blueprint('session', __name__)

@bp.route('/session/history')
def history():

    return render_template('session/history.html')

@bp.route('/session/new')
def new():

    return render_template('session/new.html')