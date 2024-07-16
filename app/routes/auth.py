from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db, bcrypt
from app.models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/')
def home():
    return render_template('login.html')

@bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        session['user_id'] = user.user_id
        return redirect(url_for('dashboard.dashboard'))
    else:
        flash('Invalid email or password. If it\'s your first time, please go to Signup.', 'flash-error')
        return redirect(url_for('auth.home'))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Password validation
        password_requirements_met = True
        error_message = ""

        if len(password) < 8:
            password_requirements_met = False
            error_message += "Password must be at least 8 characters long. "
        if not any(char.isupper() for char in password):
            password_requirements_met = False
            error_message += "Password must include an uppercase letter. "
        if not any(char.islower() for char in password):
            password_requirements_met = False
            error_message += "Password must include a lowercase letter. "
        if not any(char.isdigit() for char in password):
            password_requirements_met = False
            error_message += "Password must include a number. "

        if password != confirm_password:
            password_requirements_met = False
            error_message += "Passwords do not match. "

        if not password_requirements_met:
            form_data = {
                'email': email,
                'fname': fname,
                'lname': lname
            }
            flash(error_message, 'flash-error')
            return render_template('signup.html', form_data=form_data)

        # Hash and store password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(email=email, first_name=fname, last_name=lname, password_hash=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully. Please login.', 'flash-success')
            return redirect(url_for('auth.home'))
        except Exception as e:
            flash('An error occurred while creating the account. Please try again.', 'flash-error')
            return render_template('signup.html')

    return render_template('signup.html')

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'flash-success')
    return redirect(url_for('auth.home'))
