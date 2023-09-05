from pathlib import Path
import pandas as pd
import numpy as np
from portfolio import portfolio, db
from portfolio.models import Languages, Content

def lang_exists(c_lang):
    cont_item = Languages.query.filter(Languages.language == c_lang).first()

    if cont_item:
        return cont_item
    else:
        return False
    
def content_exists(c_template, c_langid, c_var):    
    cont_item = Content.query.filter(Content.template == str(c_template or ''), Content.languageid == c_langid, 
                                            Content.variable == c_var).first()
    if cont_item:
        return cont_item
    else:
        return False

def load_data(sheet):
    return pd.read_excel(Path('secrets/content.xlsx'), sheet_name=sheet)

def insert_language(df):
    """This function is used to insert the languages of the portfolio
    
    Keyword arguments:
    df -- dataframe
    Return: None    
    """

    lang_exists = Languages.query.filter(Languages.language == df['language']).first()
    if not lang_exists:
        lang_item = Languages(language=df['language'])
        db.session.add(lang_item)
        db.session.commit()
        
def insert_data(df):
    """
    This function would be used to insert content in the database
    At the moment, will be importing one excel file
    when I have time to improve the project, I will give the option of 
    doing it using the own website   
    """
    
    lang_id = Languages.query.filter(Languages.language == df['language'].lower()).first().id

    content_item =  content_exists(df['template'],lang_id,df['variable'])
   
    if not content_item:        
        content_item = Content(template=df['template'],languageid=lang_id,
                               variable=df['variable'],value=df['value'])
        db.session.add(content_item)       
    else:
        content_item.value = df['value']         
    db.session.commit()
    

if __name__ == '__main__':
    portfolio.app_context().push()  

    # Insert/update the languages of the portfolio

    content_df = load_data('languages')     
    content_df.apply(insert_language,axis=1)

    # Insert/update the texts of the website

    content_df = load_data('portfolio') 
    content_df['template'].replace(np.nan, '', inplace=True)
    content_df.apply(insert_data,axis=1)
    
    # Insert/update the content of the portfolio

    content_df = load_data('content')     
    content_df.apply(insert_data,axis=1)
    

