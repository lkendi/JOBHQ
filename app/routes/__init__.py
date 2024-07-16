from flask import Blueprint

def register_routes(app):
    from .auth import bp as auth_bp
    from .dashboard import bp as dashboard_bp
    from .applications import bp as applications_bp
    from .profile import bp as profile_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(applications_bp)
    app.register_blueprint(profile_bp)
