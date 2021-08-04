from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g
import requests

bp = Blueprint('exercise', __name__)

@bp.route('/exercise/history')
def history():

    return render_template('exercise/history.html')