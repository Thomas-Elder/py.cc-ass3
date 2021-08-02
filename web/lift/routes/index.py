from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, g

bp = Blueprint('', __name__)

@bp.route('/')
@bp.route('/index')
def index():

    return render_template('index.html')