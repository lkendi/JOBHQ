import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Application
from flask_testing import TestCase
from datetime import date

class TestRoutes(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()
        self.user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(self.user)
        db.session.commit()
        self.client.post('/login', data=dict(email='test@example.com', password='password'))

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_dashboard_route(self):
        response = self.client.get(url_for('dashboard.dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_applications_route(self):
        response = self.client.get(url_for('applications.applications'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My Applications', response.data)

    def test_add_application(self):
        response = self.client.post(url_for('applications.add_application'), data=dict(
            company='Test Company',
            position='Test Position',
            status='Applied',
            application_date=date.today(),
            notes='Test notes',
            user_id=self.user.id
        ))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after a successful post

        application = Application.query.filter_by(company='Test Company').first()
        self.assertIsNotNone(application)
        self.assertEqual(application.position, 'Test Position')

    def test_update_application(self):
        application = Application(
            company='Test Company',
            position='Test Position',
            status='Applied',
            application_date=date.today(),
            user_id=self.user.id
        )
        db.session.add(application)
        db.session.commit()

        response = self.client.post(url_for('applications.update_application', id=application.id), data=dict(
            company='Updated Company',
            position='Updated Position',
            status='Interview',
            application_date=date.today(),
            notes='Updated notes'
        ))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after a successful post

        application = Application.query.get(application.id)
        self.assertEqual(application.company, 'Updated Company')
        self.assertEqual(application.position, 'Updated Position')
        self.assertEqual(application.status, 'Interview')

    def test_delete_application(self):
        application = Application(
            company='Test Company',
            position='Test Position',
            status='Applied',
            application_date=date.today(),
            user_id=self.user.id
        )
        db.session.add(application)
        db.session.commit()

        response = self.client.post(url_for('applications.delete_application', id=application.id))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after a successful post

        application = Application.query.get(application.id)
        self.assertIsNone(application)

    def test_profile_route(self):
        response = self.client.get(url_for('profile.profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Profile', response.data)

if __name__ == '__main__':
    unittest.main()
