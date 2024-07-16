from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    profile_picture = db.Column(db.String(255))
    bio = db.Column(db.String(150))
    applications = db.relationship('Application', backref='user', lazy=True)
