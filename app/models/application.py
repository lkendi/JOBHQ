from app import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    application_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
