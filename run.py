from app import create_app
from app.extensions import db
from flask_migrate import Migrate
from app.models import *  # So Flask-Migrate sees the models

from alembic.config import Config
from alembic import command
import os

app = create_app()
migrate = Migrate(app, db)

if os.environ.get("RENDER"):  # Only triggers on Render
    try:
        print("Running Alembic upgrade on Render...")
        alembic_cfg = Config("migrations/alembic.ini")
        command.upgrade(alembic_cfg, "head")  # ✅ Apply all migrations
    except Exception as e:
        print("Alembic upgrade failed:", e)

if __name__ == "__main__":
    app.run()
