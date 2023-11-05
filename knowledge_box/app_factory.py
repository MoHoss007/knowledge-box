from flask import Flask
from knowledge_box.home.views import home
from knowledge_box.auth.views import auth
from knowledge_box.add_passage.views import add_passage
from knowledge_box.generate_questions.views import generate_questions


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SECRET_KEY"] = "8f1c53363ab158468a956baf"

    from knowledge_box.models import db
    db.init_app(app)

    from knowledge_box.models import bcrypt
    bcrypt.init_app(app)

    from knowledge_box.models import login_manager
    login_manager.init_app(app)

    app.app_context().push()

    # Register the blueprints
    app.register_blueprint(home, url_prefix="")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(add_passage, url_prefix="/add_passage")
    app.register_blueprint(generate_questions, url_prefix="/generate_questions")

    return app
