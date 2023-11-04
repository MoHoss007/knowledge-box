from flask import Flask
from blog.home.views import home

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(home, url_prefix="")
