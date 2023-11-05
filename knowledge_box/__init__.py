# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from knowledge_box.home.views import home
# from knowledge_box.auth.views import auth
# from knowledge_box.add_passage.views import add_passage
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SECRET_KEY"] = "8f1c53363ab158468a956baf"
# db = SQLAlchemy(app)
# app.app_context().push()
#
# # Register the blueprints
# app.register_blueprint(home, url_prefix="")
# app.register_blueprint(auth, url_prefix="/auth")
# app.register_blueprint(add_passage, url_prefix="/add_passage")
