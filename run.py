from app import create_app
from app.extensions import db
from flask_migrate import Migrate
from app.models import *  # So Flask-Migrate sees the models

app = create_app()
migrate = Migrate(app, db)
