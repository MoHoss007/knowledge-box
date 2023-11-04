from flask import Flask
from blog.home.views import home
from blog.auth.views import auth


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SECRET_KEY"] = "8f1c53363ab158468a956baf"

    from blog.models import db
    db.init_app(app)

    app.app_context().push()

    # Register the blueprints
    app.register_blueprint(home, url_prefix="")
    app.register_blueprint(auth, url_prefix="/auth")

    return app
