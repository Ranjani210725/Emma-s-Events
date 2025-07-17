from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions globally
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your API key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'  # Redirect to login page if not logged in

    # Avoid circular import issues
    from app.models import User  # You must have 'User' model with flask_login.UserMixin

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # For flask-login session management

    # Register Blueprints
    from app.routes import main
    from app.auth.routes import auth

    app.register_blueprint(auth)
    app.register_blueprint(main)

    # Create DB tables
    with app.app_context():
        db.create_all()

    return app
