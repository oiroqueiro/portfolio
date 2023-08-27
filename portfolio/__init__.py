from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

portfolio = Flask(__name__)
portfolio.config.from_object(Config)

# Emails
mail = Mail(portfolio)

# Database
db = SQLAlchemy(portfolio)
migrate = Migrate(portfolio, db)

# Login
csrf = CSRFProtect(portfolio)
login = LoginManager(portfolio)

from portfolio import routes, models