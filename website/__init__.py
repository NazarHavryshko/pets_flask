from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__, template_folder='templates', static_folder='templates/static')


def create_app(config):
    app.config.from_object(config)
    db.init_app(app)

    # register blueprint
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    # connection login manager
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # create database tables
    from .models import Users
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app
