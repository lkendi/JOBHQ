from flask import Blueprint, render_template, session, redirect, url_for

bp = Blueprint('settings', __name__)

@bp.route('/settings')
def settings():
    if 'user_id' not in session:
        return redirect(url_for('auth.home'))
    return render_template('settings.html')
