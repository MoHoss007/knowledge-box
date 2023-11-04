from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog.home.views import home

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "8f1c53363ab158468a956baf"
db = SQLAlchemy(app)
app.app_context().push()

# Register the blueprints
app.register_blueprint(home, url_prefix="")
