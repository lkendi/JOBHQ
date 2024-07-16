import unittest
from flask import session
from app import create_app, db
from app.models import User
from flask_bcrypt import Bcrypt

class TestAuthRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        with self.app.app_context():
            db.create_all()
            bcrypt = Bcrypt(self.app)
            hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
            user = User(email='test@example.com', first_name='Test', last_name='User', password_hash=hashed_password)
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login(self):
        response = self.client.post('/auth/login', data=dict(email='test@example.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['user_id'], 1)

    # Add more tests...

if __name__ == '__main__':
    unittest.main()
