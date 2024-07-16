from datetime import datetime
from app.models.application import Application
from app import db

def get_dashboard_data(from_date=None, to_date=None):
    query = db.session.query(Application)

    if from_date:
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        query = query.filter(Application.application_date >= from_date)
    if to_date:
        to_date = datetime.strptime(to_date, '%Y-%m-%d')
        query = query.filter(Application.application_date <= to_date)

    applications_submitted = query.count()
    interviews_scheduled = query.filter(Application.status == 'interview_scheduled').count()
    offers_received = query.filter(Application.status == 'offer_received').count()
    jobs_accepted = query.filter(Application.status == 'job_accepted').count()

    # Assuming the application_date is in the format '%Y-%m-%d'
    applications_overview = {
        'labels': [a.application_date.strftime('%B') for a in query.all()],
        'data': [query.filter(db.extract('month', Application.application_date) == month).count() for month in range(1, 13)]
    }
    interviews_overview = {
        'labels': [a.application_date.strftime('%B') for a in query.filter(Application.status == 'interview_scheduled').all()],
        'data': [query.filter(db.extract('month', Application.application_date) == month, Application.status == 'interview_scheduled').count() for month in range(1, 13)]
    }
    offers_overview = {
        'labels': [a.application_date.strftime('%B') for a in query.filter(Application.status == 'offer_received').all()],
        'data': [query.filter(db.extract('month', Application.application_date) == month, Application.status == 'offer_received').count() for month in range(1, 13)]
    }
    jobs_overview = {
        'labels': [a.application_date.strftime('%B') for a in query.filter(Application.status == 'job_accepted').all()],
        'data': [query.filter(db.extract('month', Application.application_date) == month, Application.status == 'job_accepted').count() for month in range(1, 13)]
    }

    data = {
        'applications_submitted': applications_submitted,
        'interviews_scheduled': interviews_scheduled,
        'offers_received': offers_received,
        'jobs_accepted': jobs_accepted,
        'applications_overview': applications_overview,
        'interviews_overview': interviews_overview,
        'offers_overview': offers_overview,
        'jobs_overview': jobs_overview,
    }

    return data
