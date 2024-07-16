from flask import Blueprint, render_template, session, redirect, url_for

bp = Blueprint('notifications', __name__)

@bp.route('/notifications')
def notifications():
    if 'user_id' not in session:
        return redirect(url_for('auth.home'))
    return render_template('notifications.html')
