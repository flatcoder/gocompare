from flask import Flask
from app.config import app_config

def create_app(env_name, db):
    app = Flask(__name__) #, static_url_path='/lib', static_folder='../node_modules')
    app.config.from_object(app_config[env_name])
    # if using auth...
    # user_manager = UserManager(app, db, User)
    db.init_app(app)
    # db.create_all()
    return app #, user_manager
