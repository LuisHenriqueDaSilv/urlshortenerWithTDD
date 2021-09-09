from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='./public'
)
# App configs
app.config.from_object('config')

# Logger configs
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(
    filename='app/logs/logs.log',
    filemode='a+',
    level=logging.ERROR,
    format=log_format
)

# Database configs
db = SQLAlchemy(app)
migrate = Migrate(
    app,
    db,
    directory='./app/database/migrations'
)

# Routes
from .routes import router
app.register_blueprint(router)

# Database models (used in migrations)
from .database.models import (
    ShortedUrl
)
