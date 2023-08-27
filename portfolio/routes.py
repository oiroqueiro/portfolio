from flask import render_template, send_from_directory, request, redirect, url_for, flash
from portfolio import portfolio
from portfolio.emails import send_email
from flask_login import current_user, login_user, logout_user
from portfolio.forms import LoginForm
from portfolio.models import Languages, Content, Users


portfolio.app_context().push()

languages = list([str(l) for l in Languages.get_all()])

@portfolio.route('/')
@portfolio.route('/index/')
@portfolio.route('/<lang>/index/')
def index(lang=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided
        
    menu_home = Content.get_value('',lang,'menu_home')['value']
    menu_about = Content.get_value('',lang,'menu_about')['value']
    menu_contact = Content.get_value('',lang,'menu_contact')['value']
    menu_projects = Content.get_value('',lang,'menu_projects')['value']
    get_touch = Content.get_value('',lang,'get_touch')['value']
    foot = Content.get_value('',lang,'foot')['value']

    if lang == 'en':
        hello = "Hey, I’m"
        name = 'Oscar Iglesias'
        subtitle = 'Data Analyst & ERP Developer Analyst. Welcome to my Portfolio.'        
    elif lang == 'es':    
        hello = 'Hola, soy'
        name = 'Oscar Iglesias'
        subtitle = 'Analista de Datos & Analista Desarrollador de ERP. Bienvenid@ a mi Portfolio.'
                   
    return render_template('index.html', lang=lang, languages=languages,
                           menu_home=menu_home, menu_about=menu_about, 
                           menu_contact=menu_contact, menu_projects=menu_projects, 
                           hello=hello, name=name, subtitle=subtitle, get_touch=get_touch, 
                           foot=foot)

@portfolio.route('/about/')
@portfolio.route('/<lang>/about/')
def about(lang=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided
        
    menu_home = Content.get_value('',lang,'menu_home')['value']
    menu_about = Content.get_value('',lang,'menu_about')['value']
    menu_contact = Content.get_value('',lang,'menu_contact')['value']
    menu_projects = Content.get_value('',lang,'menu_projects')['value']    
    foot = Content.get_value('',lang,'foot')['value']

    if lang == 'en':
        hello = "Hi,I’m Oscar Iglesias, Data Analyst and ERP Analyst Developer"
        parragraph1 = "I'm living in Ourense, a small city of Spain with my wife and 2 little girls."
        parragraph2 = 'I love working with data. During my professional experience, I got the chance to work with many types of\
                       databases and acquire a great experience helping stakeholders to get more information and discover good\
                       insights because of my skills in visualisation as well.'
        parragraph3 = 'Then, when my youngest baby was ready to be born I had the chance to join Ironhack to improve my skills of\
                       data mining and learn much more about analysis and artificial intelligence. During this time I had to face\
                       many challenges that the teaching team provided us which I could solve, making me feel more confident with\
                       my skills and learning and creating projects (like my final project, Ironhack repository) that could help others\
                       to improve their skills too.'
        parragraph4 = 'I consider myself a team player with great adaptability and autonomy as I had to learn almost by myself and\
                       start to create features for different ERP along the years. My work colleagues would say I am a hard-working\
                       person that doesn’t hesitate to help others when they need to deliver an urgent job so they can reach on\
                       time.'        
        parragraph5 = 'During my career I helped companies to manage their ERPs and Data so their employees, my colleagues, could dedicate more time to other tasks and be more productive.'
        parragraph6 = ''
        skills_title = 'My Skills'
        skill1 = 'Creative Problem Solving.'
        skill2 = 'Responsible.'
        skill3 = 'Adaptability.'
    elif lang == 'es':    
        hello = 'Hola, soy Oscar Iglesias, Analista de Datos y Analista Desarrollador de ERP.'
        parragraph1 = "Estoy viviendo Ourense, una pequeña ciudad de España con mi mujer y mis dos niñas."
        parragraph2 = 'Me encanta trabajar con datos. Durante toda mi carrera profesional, tuve la oportunidad de trabajar con muchos tipos de\
                       bases de datos y adquirir una gran experiencia ayudando a las partes interesadas a obtener más información y descrubrir\
                       claves esclarecedoras debido, también, a mis habilidades en visualización de datos.'
        parragraph3 = 'Entonces, cuando mi hija más pequeña estaba preparada para nacer, tuve la oportunidad de unirme al bootcamp de análisis\
                       de datos de Ironhack para mejorar mis habilidades de minería de datos y aprender mucho más de análisis e inteligencia artificial.\
                       Durante este tiempo tuve que superar muchos retos que el equipo de enseñanza nos propuso, haciéndome sentir más confianza\
                       en mis habilidades y aprendiendo y creando proyectos (como mi proyecto final, Ironhack repository) que podrían ayudar a otros\
                       también a incrementar sus habilidades.'
        parragraph4 = 'Me considero a mi mismo un buen compañsero de trabajo con gran adaptabilidad y autonomía ya que he tenido que aprender por mi mismo\
                       a crear nuevas funcionalidades en los diferentes ERP a lo largo de los años. Mis compañeros de trabajo dirían que soy una persona trabajadora\
                       que no duda en ayudar a otros cuando lo necesitan.'        
        parragraph5 = 'Durante mi carrera he ayudado a muchas empresas a manejar su ERP y datos de manera que sus empleados, y en muchos casos mis compañeros, podían dedicar más tiempo a otras tareas y ser más productivos.'
        parragraph6 = ''
        skills_title = 'Mis habilidades'
        skill1 = 'Resolución creativa de problemas.'
        skill2 = 'Responsable.'
        skill3 = 'Adaptabilidad.'

    return render_template('about/index.html', lang=lang, languages=languages, 
                           menu_home=menu_home, menu_about=menu_about, 
                           menu_contact=menu_contact, menu_projects=menu_projects,  
                           hello=hello, parragraph1=parragraph1, parragraph2=parragraph2, 
                           parragraph3=parragraph3, parragraph4=parragraph4, parragraph5=parragraph5,
                           parragraph6=parragraph6, 
                           skills_title=skills_title, skill1=skill1, skill2=skill2, skill3=skill3,
                           foot=foot)


    return render_template('about/index.html')

@portfolio.route('/projects/')
def projects():
    return render_template('element/index.html')

@portfolio.route('/contact/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/contact/', methods=['GET', 'POST'])
def contact(lang=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided
        
    menu_home = Content.get_value('',lang,'menu_home')['value']
    menu_about = Content.get_value('',lang,'menu_about')['value']
    menu_contact = Content.get_value('',lang,'menu_contact')['value']
    menu_projects = Content.get_value('',lang,'menu_projects')['value']
    foot = Content.get_value('',lang,'foot')['value']

    if lang == 'en':
        title = "Let's Connect"        
        subtitle = "I'm excited to hear from you! Whether you have a project in mind, want to collaborate, or simply want to say hello, don't hesitate to reach out. Your ideas and thoughts matter, and I'm here to ensure your experience is exceptional. Feel free to get in touch – I'm just an email away."
        first_name = 'First Name'
        last_name = 'Last Name'
        email = 'Email'
        message = 'Type your message...'
        submit = 'Submit message'    
    elif lang == 'es':                       
        title = 'Vamos a conectar'        
        subtitle = '¡Estoy deseando saber de ti! Ya sea que tengas un proyecto en mente, quieras colaborar o simplemente quieras saludar, no dudes en comunicarte. Tus ideas y pensamientos importan, y estoy aquí para asegurar que tu experiencia sea excepcional. No dudes en ponerte en contacto, estoy a solo un correo electrónico de distancia.'
        first_name = 'Nombre'
        last_name = 'Apellidos'
        email = 'Correo Electrónico'
        message = 'Escribe tu mensaje...'
        submit = 'Enviar mensaje'        

    if request.method == 'POST':
        first_name_post = request.form['First Name']
        last_name_post = request.form['Last Name']
        email_post = request.form['Email']
        message_post = request.form['Type your message...']
        
        msg_body = f"Name: {first_name_post} {last_name_post}\n\nEmail: {email_post}\n\nMessage:\n {message_post}"        

        send_email(portfolio.config['MAIL_USERNAME'], ['info@oscarlytics.com'],        
                    'New message from Oscarlytics portfolio',msg_body)
        
        return redirect(request.url)

    return render_template('contact/index.html', lang=lang, languages=languages, 
                           menu_home=menu_home, menu_about=menu_about, 
                           menu_contact=menu_contact, menu_projects=menu_projects, 
                           title=title, subtitle=subtitle, first_name=first_name, last_name=last_name,
                           email=email, message=message, submit=submit,
                           foot=foot)

@portfolio.route('/login/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/login/', methods=['GET', 'POST'])
def login(lang=None): 
    if lang is None:
        lang='en'  # Set a default language if lang is not provided
        
    menu_home = Content.get_value('',lang,'menu_home')['value']
    menu_about = Content.get_value('',lang,'menu_about')['value']
    menu_contact = Content.get_value('',lang,'menu_contact')['value']
    menu_projects = Content.get_value('',lang,'menu_projects')['value']
    foot = Content.get_value('',lang,'foot')['value']

    if current_user.is_authenticated:
        return redirect(url_for('index', lang=lang))
        
    form = LoginForm()    

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()  
        if user is None or not user.check_password(form.password.data):               
            flash('Invalid username or password')            
            return redirect(url_for('login', lang=lang))        
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('index', lang=lang))
    
    return render_template('login.html', form=form,
                           lang=lang, languages=languages, 
                           menu_home=menu_home, menu_about=menu_about, 
                           menu_contact=menu_contact, menu_projects=menu_projects,
                           foot=foot)
    

    
@portfolio.route('/logout/')
@portfolio.route('/<lang>/logout/', methods=['GET', 'POST'])
def logout(lang=None):
    if lang is None:
        lang='en'  # Set a default language if lang is not provided
    
    logout_user()
    return redirect(url_for('index', lang=lang))

@portfolio.route('/manifest.webmanifest')
def manifest():
    return send_from_directory('static', 'manifest.webmanifest')