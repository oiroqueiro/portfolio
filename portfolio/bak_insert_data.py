from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from portfolio import portfolio, db
import os

basedir = os.path.abspath(os.path.dirname(__file__))

"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""

db = SQLAlchemy(portfolio)

from models import Languages, Portfolio

def get_language_id(language_name):
    with portfolio.app_context():
        language = Languages.query.filter_by(language=language_name).first()
        if language:
            return language.id
        return None
    
def insert_data():
    """
    This function would be used to insert data in the database
    At the moment, it will be with SQL directly, 
    when I can improve the project, I will give the option of import one file    
    """
    
    
    try:
        with portfolio.app_context():
            
            #
            # Languages
            #

            #language = Languages.query.filter_by(language='en').first()
            language = db.session.execute(db.select(Languages).filter_by(language='en').scalar_one())
            if not language:
                language = Languages(language='en')
                db.session.add(language)

            db.session.commit()

            #language = Languages.query.filter_by(language='es').first()
            language = db.session.execute(db.select(Languages).filter_by(language='es').scalar_one())
            if not language:
                language = Languages(language='es')
                db.session.add(language)
            
            db.session.commit()

            #
            # Portfolio
            #
            
            # index template #

            # english

            lang_id = get_language_id('en')

            portfolio_item = Portfolio.query.filter_by(template='index', languageid=lang_id, variable='hello').first()

            if not portfolio_item:
                portfolio_item = Portfolio(
                    template='index',
                    languageid=lang_id,
                    variable='hello',
                    value="Hey, I’m"
                )
                db.session.add(portfolio_item)

                #db.session.commit()
            else:
                # Update with the new data.
                # I will insert the same data meanwhile I don't have changes to do

                portfolio_item.value="Hey, I’m"

                #db.session.commit()

            db.session.commit()
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    print("BEGIN")
    with portfolio.app_context():
        insert_data()
