from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from app import db
from app.models.application import Application

bp = Blueprint('applications', __name__)

@bp.route('/applications')
def applications():
    if 'user_id' not in session:
        return redirect(url_for('auth.home'))
    user_id = session['user_id']
    applications = Application.query.filter_by(user_id=user_id).all()
    return render_template('applications.html', applications=applications)

@bp.route('/add_application', methods=['POST'])
def add_application():
    if 'user_id' not in session:
        return redirect(url_for('auth.home'))

    user_id = session['user_id']
    job_title = request.form.get('job_title')
    company_name = request.form.get('company_name')
    application_date = request.form.get('application_date')
    status = request.form.get('status')

    new_application = Application(
        user_id=user_id,
        job_title=job_title,
        company_name=company_name,
        application_date=application_date,
        status=status
    )
    db.session.add(new_application)
    db.session.commit()
    return redirect(url_for('applications.applications'))

@bp.route('/update_status', methods=['POST'])
def update_status():
    application_id = request.form['application_id']
    new_status = request.form['status']
    application = Application.query.get(application_id)
    if application:
        application.status = new_status
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400

@bp.route('/get_application/<int:application_id>', methods=['GET'])
def get_application(application_id):
    application = Application.query.get(application_id)
    if application:
        return jsonify({
            'id': application.id,
            'job_title': application.job_title,
            'company_name': application.company_name,
            'application_date': application.application_date.strftime('%Y-%m-%d'),
            'status': application.status
        })
    return jsonify({'error': 'Application not found'}), 404

@bp.route('/update_application', methods=['POST'])
def update_application():
    application_id = request.form['application_id']
    application = Application.query.get(application_id)
    if application:
        application.job_title = request.form['job_title']
        application.company_name = request.form['company_name']
        application.application_date = request.form['application_date']
        application.status = request.form['status']
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400
