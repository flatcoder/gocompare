from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import url_for, redirect
from app import create_app
from app.seed_db import SeedDBCommand
from app.tests import TestDDCommand
from app.models import db
from app.basket import Basket

import os

# if using auth...
# from flask_user import login_required, current_user, user_changed_password

# Environment
env = "test"
if os.getenv('FLASK_ENV') != None:
    env = os.getenv('FLASK_ENV')

# Application
app     = create_app(env, db)
migrate = Migrate(app, db)
manager = Manager(app)

# Management Commands
manager.add_command('database', MigrateCommand)
manager.add_command('seed_database', SeedDBCommand)
manager.add_command('run_tests', TestDDCommand)

# Routes
@app.route('/')
def home():
    return "See README.md, no UI presently, use Run Tests management command."

# Go!
if __name__ == '__main__':
    manager.run()

