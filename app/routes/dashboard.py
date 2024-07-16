from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from app import db
from app.models.user import User
from app.models.application import Application
from app.utils.dashboard_data import get_dashboard_data

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    user = User.query.get(user_id)
    user_applications = Application.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', user=user, user_applications=user_applications)

@bp.route('/get_dashboard_data')
def get_dashboard_data_route():
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    data = get_dashboard_data(from_date, to_date)
    return jsonify(data)
