from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate SQLAlchemy
db = SQLAlchemy()

# Instantiate Flask-Migrate
migrate = Migrate()
