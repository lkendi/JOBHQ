from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    app.config.from_object('app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from .models import user, application
        from .routes import auth, dashboard, applications, profile, settings, notifications

        # Create database tables
        db.create_all()

        # Register Blueprints
        app.register_blueprint(auth.bp)
        app.register_blueprint(dashboard.bp)
        app.register_blueprint(applications.bp)
        app.register_blueprint(profile.bp)
        app.register_blueprint(settings.bp)
        app.register_blueprint(notifications.bp)

    return app
