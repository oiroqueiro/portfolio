from pathlib import Path
import pandas as pd
import numpy as np
from portfolio import portfolio, db
from portfolio.models import Languages, Content, Projects

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
    
def project_exists(c_date, c_langid, c_projn):    
    proj_item = Projects.query.filter(Projects.date == c_date, Projects.languageid == c_langid, 
                                            Projects.project_n == c_projn).first()
    if proj_item:
        return proj_item
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

    
def insert_projects(df):
    """
    This function would be used to insert content in the database
    At the moment, will be importing one excel file
    when I have time to improve the project, I will give the option of 
    doing it using the own website   
    """
    
    df['keywords'] = df['keywords'].lower()

    lang_id = Languages.query.filter(Languages.language == df['language'].lower()).first().id

    project_item = project_exists(df['date'],lang_id,df['project_n'])
        
    if not project_item:        
        project_item = Projects(date=df['date'],languageid=lang_id,project_n=df['project_n'],
                               title=df['title'],resume=df['resume'],description=df['description'],
                               resolution=df['resolution'],keywords=df['keywords'],
                               link1=df['link1'],link2=df['link2'],link3=df['link3'],
                               link4=df['link4'],link5=df['link5'],
                               image1=df['image1'],image2=df['image2'],image3=df['image3'])
        db.session.add(project_item)       
    else:
        project_item.date = df['date']         
        project_item.project_n = df['project_n']         
        project_item.languageid = lang_id
        project_item.title = df['title']         
        project_item.resume = df['resume']         
        project_item.desccription = df['description']         
        project_item.resolution = df['resolution']         
        project_item.keywords = df['keywords']
        project_item.link1 = df['link1']         
        project_item.link2 = df['link2']         
        project_item.link3 = df['link3']         
        project_item.link4 = df['link4']         
        project_item.link5 = df['link5']     
        project_item.image1 = df['image1']    
        project_item.image2 = df['image2']    
        project_item.image3 = df['image3']    

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

    # Insert/update the projects of the portfolio

    content_df = load_data('projects')     
    content_df.replace(np.nan, '', inplace=True)
    content_df.apply(insert_projects,axis=1)

    

