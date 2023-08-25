from flask import render_template, send_from_directory, request, redirect
from portfolio import portfolio
from portfolio.emails import send_email
from portfolio.models import Languages, Content

portfolio.app_context().push()

languages = list([str(l) for l in Languages.get_all()])

@portfolio.route('/')
@portfolio.route('/index')
@portfolio.route('/<lang>/index')
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
def about():
    return render_template('about/index.html')

@portfolio.route('/projects/')
def projects():
    return render_template('element/index.html')

@portfolio.route('/contact/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/contact/', methods=['GET', 'POST'])
def contact(lang=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided       
        
    if lang == 'en':
        menu_home = 'Home'
        menu_about = 'About'
        menu_projects = 'Projects'
        menu_contact = 'Contact'        
        title = "Let's Connect"        
        subtitle = "I'm excited to hear from you! Whether you have a project in mind, want to collaborate, or simply want to say hello, don't hesitate to reach out. Your ideas and thoughts matter, and I'm here to ensure your experience is exceptional. Feel free to get in touch – I'm just an email away."
        first_name = 'First Name'
        last_name = 'Last Name'
        email = 'Email'
        message = 'Type your message...'
        submit = 'Submit message'
        foot = 'Follow me'
    elif lang == 'es':
        menu_home = 'Inicio'
        menu_about = 'Sobre mí'
        menu_projects = 'Proyectos'
        menu_contact = 'Contacto'                
        title = 'Vamos a conectar'        
        subtitle = '¡Estoy deseando saber de ti! Ya sea que tengas un proyecto en mente, quieras colaborar o simplemente quieras saludar, no dudes en comunicarte. Tus ideas y pensamientos importan, y estoy aquí para asegurar que tu experiencia sea excepcional. No dudes en ponerte en contacto, estoy a solo un correo electrónico de distancia.'
        first_name = 'Nombre'
        last_name = 'Apellidos'
        email = 'Correo Electrónico'
        message = 'Escribe tu mensaje...'
        submit = 'Enviar mensaje'
        foot = 'Sígueme'

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

@portfolio.route('/manifest.webmanifest')
def manifest():
    return send_from_directory('static', 'manifest.webmanifest')