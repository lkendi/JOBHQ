"""Models module"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    """
    User model class.

    Attributes:
        user_id (db.Column): Unique identifier for the user.
        email (db.Column): Unique email address of the user.
        first_name (db.Column): First name of the user.
        last_name (db.Column): Last name of the user.
        password_hash (db.Column): Hashed password of the user.
        created_at (db.Column): Timestamp when the user was created.
        profile_picture (db.Column): URL of the user's profile picture.
        bio (db.Column): Short bio of the user.
        applications (db.relationship): List of applications made by the user.
    """
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    profile_picture = db.Column(db.String(255))
    bio = db.Column(db.String(150))
    applications = db.relationship('Application', backref='user', lazy=True)

class Application(db.Model):
    """
    Application model class.

    Attributes:
        id (db.Column): Unique identifier for the application.
        company_name (db.Column): Name of the company.
        job_title (db.Column): Title of the job.
        application_date (db.Column): Date the application was made.
        status (db.Column): Status of the application.
        user_id (db.Column): Foreign key referencing the user who made the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    application_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
