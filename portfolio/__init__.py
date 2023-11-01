from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flaskext.markdown import Markdown
from elasticsearch import Elasticsearch

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

# Markdown for the detail of the project
Markdown(portfolio)

# Elasticsearch

# portfolio.elasticsearch = Elasticsearch(portfolio.config['ELASTICSEARCH_URL'],
#        ssl_assert_fingerprint=portfolio.config['ELASTICSEARCH_FINGERPR']) \
#        if (portfolio.config['ELASTICSEARCH_URL'] and
#            portfolio.config['ELASTICSEARCH_FINGERPR']) else None

portfolio.elasticsearch = Elasticsearch([str(portfolio.config['ELASTICSEARCH_URL'])],
                        basic_auth=('elastic', str(portfolio.config['ELASTIC_PASSWORD']))) \
    if (portfolio.config['ELASTICSEARCH_URL']) else None

from portfolio import routes, models
