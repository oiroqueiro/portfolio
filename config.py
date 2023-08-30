class Config(object):
    import os

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Secret Key

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

    # Emailing
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL') == 'True')
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS') == 'True')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')        
    MAIL_RECIPIENT = os.environ.get('MAIL_RECIPIENT')

    # Database

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'portfolio.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Custom Login url

    PORTFOLIO_LOGIN_URL = os.environ.get('PORTFOLIO_LOGIN_URL') or 'login'
    PORTFOLIO_LOGOUT_URL = os.environ.get('PORTFOLIO_LOGOUT_URL') or 'logout'