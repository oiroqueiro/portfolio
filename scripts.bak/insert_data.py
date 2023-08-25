from flask_sqlalchemy import SQLAlchemy
from portfolio import portfolio

from portfolio.models import Languages, Portfolio

app = portfolio.app
db = portfolio.db

def insert_data():
    """
    This function would be used to insert data in the database
    At the moment, it will be with SQL directly, 
    when I can improve the project, I will give the option of import one file    
    """

    with app.app_context():

        language = Languages(language='en')
        db.session.add(language)

        language = Languages(language='es')
        db.session.add(language)

        db.session.commit()

if __name__ == '__main__':
    insert_data()