from flask import render_template, send_from_directory, request, redirect, \
    url_for, flash, abort
from portfolio import portfolio, db
from portfolio.emails import send_email
from flask_login import current_user, login_user, logout_user
from portfolio.forms import LoginForm
from portfolio.models import Languages, Content, Users, Projects
import readtime

portfolio.app_context().push()

# Managing the context processor with multilanguage and title slugs for projects


@portfolio.before_request
def set_lang(lang=None):
    request.lang = request.args.get('lang', lang)


def set_slug(slug=None):
    request.title_slug = request.args.get('title_slug', slug)


@portfolio.context_processor
def inject_data():
    lang = request.lang
    title_slug = request.title_slug

    languages = list([str(l) for l in Languages.get_all()])

    try:
        menu_home = str(Content.get_value(
            '', lang, 'menu_home')['value'] or '')
        menu_about = Content.get_value('', lang, 'menu_about')['value']
        menu_contact = Content.get_value('', lang, 'menu_contact')['value']
        menu_projects = Content.get_value('', lang, 'menu_projects')['value']
        menu_manage = Content.get_value('', lang, 'menu_manage')['value']
        menu_manage_home = Content.get_value(
            '', lang, 'menu_manage_home')['value']
        menu_manage_about = Content.get_value(
            '', lang, 'menu_manage_about')['value']
        menu_manage_projects = Content.get_value(
            '', lang, 'menu_manage_projects')['value']
        menu_manage_contact = Content.get_value(
            '', lang, 'menu_manage_contact')['value']
        menu_manage_logout = Content.get_value(
            '', lang, 'menu_manage_logout')['value']
        foot = Content.get_value('', lang, 'foot')['value']
    except KeyError:
        abort(404)

    return dict(languages=languages,
                menu_home=menu_home, menu_about=menu_about,
                menu_contact=menu_contact, menu_projects=menu_projects,
                menu_manage=menu_manage, menu_manage_home=menu_manage_home,
                menu_manage_about=menu_manage_about,
                menu_manage_projects=menu_manage_projects,
                menu_manage_contact=menu_manage_contact,
                menu_manage_logout=menu_manage_logout, foot=foot,
                title_slug=title_slug)

# index


@portfolio.route('/')
@portfolio.route('/index/')
@portfolio.route('/<lang>/index/')
def index(lang=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_slug(title_slug)

    get_touch = Content.get_value('', lang, 'get_touch')['value']

    hello = str(Content.get_value('index', lang, 'hello')['value'] or '')
    name = str(Content.get_value('index', lang, 'name')['value'] or '')
    subtitle = str(Content.get_value('index', lang, 'subtitle')['value'] or '')

    return render_template('index.html', lang=lang, hello=hello, name=name,
                           subtitle=subtitle, get_touch=get_touch)

# about


@portfolio.route('/about/')
@portfolio.route('/<lang>/about/')
def about(lang=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_slug(title_slug)

    hello = str(Content.get_value('about', lang, 'hello')['value'] or '')
    parragraph1 = str(Content.get_value('about', lang, 'parragraph1')['value']
                      or '')
    parragraph2 = str(Content.get_value('about', lang, 'parragraph2')['value']
                      or '')
    parragraph3 = str(Content.get_value('about', lang, 'parragraph3')['value']
                      or '')
    parragraph4 = str(Content.get_value('about', lang, 'parragraph4')['value']
                      or '')
    parragraph5 = str(Content.get_value('about', lang, 'parragraph5')['value']
                      or '')
    parragraph6 = str(Content.get_value('about', lang, 'parragraph6')['value']
                      or '')
    skills_title = str(Content.get_value('about', lang, 'skills_title')['value']
                       or '')
    skill1 = str(Content.get_value('about', lang, 'skill1')['value'] or '')
    skill2 = str(Content.get_value('about', lang, 'skill2')['value'] or '')
    skill3 = str(Content.get_value('about', lang, 'skill3')['value'] or '')
    youtube = str(Content.get_value('about', lang, 'youtube')['value'] or '')

    more = str(Content.get_value('', lang, 'more')['value'] or '')

    return render_template('about/index.html', lang=lang, hello=hello,
                           parragraph1=parragraph1, parragraph2=parragraph2,
                           parragraph3=parragraph3, parragraph4=parragraph4,
                           parragraph5=parragraph5, parragraph6=parragraph6,
                           skills_title=skills_title, skill1=skill1,
                           skill2=skill2, skill3=skill3, more=more,
                           youtube=youtube)

# projects


@portfolio.route('/projects/', methods=['GET', 'POST'])
@portfolio.route('/projects/<keyw>/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/projects/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/projects/<keyw>/', methods=['GET', 'POST'])
def projects(lang=None, keyw=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_slug(title_slug)
    langid = Languages.getid(lang)

    all_keywords, keywords_freq = Projects.get_all_keyws_and_freq(langid)

    keyw_title = str(Content.get_value('', lang, 'keyw_title')['value'] or '')
    more = str(Content.get_value('', lang, 'more')['value'] or '')
    previous = str(Content.get_value('', lang, 'previous')['value'] or '')
    next = str(Content.get_value('', lang, 'next')['value'] or '')

    page = request.args.get('page', 1, type=int)

    projs = Projects.query

    if keyw:
        projs = projs.filter(Projects.languageid == langid,
                             Projects.keywords.like(f"%{keyw}%"))
    else:
        projs = projs.filter(Projects.languageid == langid)

    projs = (
        projs
        .order_by(Projects.date.desc(), Projects.project_n.desc())
        .paginate(page=page, per_page=portfolio.config['PROJECTS_PAGE'],
                  error_out=False)
    )

    print(f"*** {keyw}")
    [print(f"*** {p}") for p in projs.items]

    next_url = url_for('projects', lang=lang, page=projs.next_num) \
        if projs.has_next else None

    prev_url = url_for('projects', lang=lang, page=projs.prev_num) \
        if projs.has_prev else None

    return render_template('projects/index.html', lang=lang, projs=projs.items,
                           page=page, next_url=next_url, prev_url=prev_url,
                           more=more, previous=previous, next=next,
                           all_keywords=all_keywords,
                           keywords_freq=keywords_freq, keyw_title=keyw_title)


@portfolio.route('/project/<title_slug>/')
@portfolio.route('/<lang>/project/<title_slug>/')
def project(lang=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_slug(title_slug)
    set_lang(lang)

    keyw_title = str(Content.get_value('', lang, 'keyw_title')['value'] or '')
    read = str(Content.get_value('', lang, 'read')['value'] or '')

    project = Projects.get_by_slug(title_slug)
    time_reading = str(readtime.
                       of_markdown(" ".join([project.resume,
                                             project.exposition,
                                             project.action,
                                             project.resolution]))
                       ).replace('read', read)

    return render_template('projects/project_detail.html', lang=lang,
                           title_slug=title_slug, project=project,
                           keyw_title=keyw_title, time_reading=time_reading)


# contact

@portfolio.route('/contact/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/contact/', methods=['GET', 'POST'])
def contact(lang=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_slug(title_slug)

    title = str(Content.get_value('contact', lang, 'title')['value'] or '')
    subtitle = str(Content.get_value('contact', lang, 'subtitle')['value']
                   or '')
    first_name = str(Content.get_value('contact', lang, 'first_name')['value']
                     or '')
    last_name = str(Content.get_value('contact', lang, 'last_name')['value']
                    or '')
    email = str(Content.get_value('contact', lang, 'email')['value'] or '')
    message = str(Content.get_value('contact', lang, 'message')['value'] or '')
    submit = str(Content.get_value('contact', lang, 'submit')['value'] or '')
    email_subject = str(Content.get_value('contact', lang, 'email_subject'
                                          )['value'] or '')

    if request.method == 'POST':
        first_name_post = request.form['First Name']
        last_name_post = request.form['Last Name']
        email_post = request.form['Email']
        message_post = request.form['Type your message...']

        msg_body = f"Name: {first_name_post} {last_name_post}\n\nEmail: \
            {email_post}\n\nMessage:\n {message_post}"

        send_email(portfolio.config['MAIL_USERNAME'],
                   portfolio.config['MAIL_RECIPIENT'], email_subject, msg_body)

        return redirect(request.url)

    return render_template('contact/index.html', lang=lang, title=title,
                           subtitle=subtitle, first_name=first_name,
                           last_name=last_name, email=email, message=message,
                           submit=submit)

# login


@portfolio.route(f"/{portfolio.config['PORTFOLIO_LOGIN_URL']}/",
                 methods=['GET', 'POST'])
@portfolio.route(f"/<lang>/{portfolio.config['PORTFOLIO_LOGIN_URL']}/",
                 methods=['GET', 'POST'])
def login(lang=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_slug(title_slug)

    if current_user.is_authenticated:
        return redirect(url_for('index', lang=lang))

    form = LoginForm()

    form.username.label.text = str(Content.get_value('', lang, 'username'
                                                     )['value'] or '')
    form.password.label.text = str(Content.get_value('', lang, 'password'
                                                     )['value'] or '')
    form.remember_me.label.text = str(Content.get_value('', lang, 'rememberme'
                                                        )['value'] or '')
    form.submit.label.text = str(Content.get_value('', lang, 'signin')['value']
                                 or '')

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(Content.get_value('', lang, 'errorlogin')['value'])
            return redirect(url_for('login', lang=lang))

        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('index', lang=lang))

    return render_template('login.html', form=form, lang=lang,
                           signin=form.submit.label.text)

# logout


@portfolio.route(f"/{portfolio.config['PORTFOLIO_LOGOUT_URL']}/",
                 methods=['GET', 'POST'])
@portfolio.route(f"/<lang>/{portfolio.config['PORTFOLIO_LOGOUT_URL']}/",
                 methods=['GET', 'POST'])
def logout(lang=None, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_slug(title_slug)

    logout_user()
    return redirect(url_for('index', lang=lang))

# manifest


@portfolio.route('/manifest.webmanifest')
def manifest():
    return send_from_directory('static', 'manifest.webmanifest')
