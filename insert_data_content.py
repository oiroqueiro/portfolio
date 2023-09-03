from pathlib import Path
import pandas as pd
from portfolio import portfolio, db
from portfolio.models import Languages, Content

def content_exists(c_template, c_langid, c_var):
    cont_item = Content.query.filter(Content.template == c_template, Content.languageid == c_langid, 
                                            Content.variable == c_var).first()
    if cont_item:
        return cont_item
    else:
        return False

def load_data():
    return pd.read_excel(Path('secrets/content.xlsx'), sheet_name='content')

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
    content_df = load_data()
    #insert_data(content_df)    
    content_df.apply(insert_data,axis=1)
    

