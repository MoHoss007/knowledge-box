import json
from flask import Flask
from knowledge_box.views.home import home
from knowledge_box.views.auth import auth
from knowledge_box.views.add_passage import add_passage
from knowledge_box.views.generate_questions import generate_questions
from knowledge_box.services.ocr_service import OCR


def create_app(config_path="config.json"):
    app = Flask(__name__)

    with open(config_path) as config_file:
        config = json.load(config_file)
        db_config = config["DATABASE"]

    app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{db_config["USERNAME"]}:{db_config["PASSWORD"]}@' \
                                            f'{db_config["HOST"]}:{db_config["PORT"]}/{db_config["NAME"]}'
    app.config["SECRET_KEY"] = config["SECRET_KEY"]
    app.config['PORT'] = config["PORT"]
    app.config['DEBUG'] = config["DEBUG"]
    app.topics = config["TOPICS"]
    ocr_service = OCR(config["API_KEY"])
    app.ocr_service = ocr_service

    from knowledge_box.extensions import db
    db.init_app(app)

    from knowledge_box.models.user import bcrypt
    bcrypt.init_app(app)

    from knowledge_box.models.user import login_manager
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    app.app_context().push()

    # Register the blueprints
    app.register_blueprint(home, url_prefix="")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(add_passage, url_prefix="/add_passage")
    app.register_blueprint(generate_questions, url_prefix="/generate_questions")

    return app

