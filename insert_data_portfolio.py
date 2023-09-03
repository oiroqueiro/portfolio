from portfolio import portfolio, db
from portfolio.models import Languages, Content

def menu_exists(menu_langid, menu_var):
    cont_item = Content.query.filter(Content.template == '', Content.languageid == menu_langid, 
                                            Content.variable == menu_var).first()
    if cont_item:
        return cont_item
    else:
        return False

def insert_data():
    """
    This function would be used to insert content in the database
    At the moment, it will be with SQL directly 
    when I can improve the project, I will give the option of import one file    
    """
        
    # Languages of the portfolio

    lang_exists = Languages.query.filter(Languages.language == 'en').first()
    if not lang_exists:
        language = Languages(language='en')
        db.session.add(language)

    lang_exists = Languages.query.filter(Languages.language == 'es').first()
    if not lang_exists:
        language = Languages(language='es')
        db.session.add(language)

    db.session.commit()

    # Texts of the website that are not content
    
    # English

    lang_id = Languages.query.filter(Languages.language == 'en').first().id

    portfolio_item =  menu_exists(lang_id, 'menu_home')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_home',value='Home')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_about')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_about',value='About')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_projects')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_projects',value='Projects')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_contact')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_contact',value='Contact')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage',value='Manage Content')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_home')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_home',value='Edit Home')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_about')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_about',value='Edit About')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_projects')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_projects',value='Edit Projects')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_contact')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_contact',value='Edit Contact')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_logout')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_logout',value='Logout')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'get_touch')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='get_touch',value='Get in touch')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'foot')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='foot',value='Follow me')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'signin')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='signin',value='Sign In')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'username')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='username',value='Username')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'password')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='password',value='Password')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'rememberme')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='rememberme',value='Remember Me')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'errorlogin')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='errorlogin',value='Invalid username or password')
        db.session.add(portfolio_item)

    # Spanish

    lang_id = Languages.query.filter(Languages.language == 'es').first().id

    portfolio_item =  menu_exists(lang_id, 'menu_home')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_home',value='Inicio')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_about')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_about',value='Sobre mí')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_projects')

    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_projects',value='Proyectos')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_contact')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_contact',value='Contacto')
        db.session.add(portfolio_item)
        
    portfolio_item =  menu_exists(lang_id, 'menu_manage')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage',value='Gestionar Contenido')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_home')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_home',value='Editar Inicio')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_about')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_about',value='Editar Sobre Mí')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_projects')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_projects',value='Editar Proyectos')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_contact')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_contact',value='Editar Contacto')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'menu_manage_logout')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='menu_manage_logout',value='Cerrar Sesión')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'get_touch')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='get_touch',value='Ponte en contacto')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'foot')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='foot',value='Sígueme')
        db.session.add(portfolio_item)                

    portfolio_item =  menu_exists(lang_id, 'signin')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='signin',value='Inicio Sesión')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'username')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='username',value='Nombre de Usuario')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'password')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='password',value='Contraseña')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'rememberme')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='rememberme',value='Recuérdame')
        db.session.add(portfolio_item)

    portfolio_item =  menu_exists(lang_id, 'errorlogin')
   
    if not portfolio_item:        
        portfolio_item = Content(template='',languageid=lang_id,variable='errorlogin',value='Nombre de Usuario o Contraseña no válidos')
        db.session.add(portfolio_item)

    db.session.commit()

if __name__ == '__main__':
    portfolio.app_context().push()  
    insert_data()

