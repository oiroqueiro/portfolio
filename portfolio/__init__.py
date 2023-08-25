from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

portfolio = Flask(__name__)
portfolio.config.from_object(Config)

mail = Mail(portfolio)

db = SQLAlchemy(portfolio)
migrate = Migrate(portfolio, db)

from portfolio import routes, models