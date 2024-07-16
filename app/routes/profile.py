from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app import db
from app.models.user import User

bp = Blueprint('profile', __name__)

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    user = User.query.get(user_id)

    if request.method == 'POST':
        user.first_name = request.form['fname']
        user.last_name = request.form['lname']
        user.email = request.form['email']
        user.bio = request.form['bio']
        db.session.commit()
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('profile.profile'))

    return render_template('profile.html', user=user)
