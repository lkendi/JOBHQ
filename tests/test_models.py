import unittest
from datetime import date
from app import create_app, db
from app.models import User, Application

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    def test_application_model(self):
        application = Application(
            company='Test Company',
            position='Test Position',
            status='Applied',
            application_date=date.today(),
            user_id=self.user.id
        )
        db.session.add(application)
        db.session.commit()

        application = Application.query.filter_by(company='Test Company').first()
        self.assertIsNotNone(application)
        self.assertEqual(application.position, 'Test Position')
        self.assertEqual(application.status, 'Applied')
        self.assertEqual(application.application_date, date.today())
        self.assertEqual(application.user_id, self.user.id)

if __name__ == '__main__':
    unittest.main()