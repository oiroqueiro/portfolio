from flask import render_template, send_from_directory, request, redirect, \
    url_for, flash, abort, jsonify
from portfolio import portfolio, db
from portfolio.emails import send_email
from flask_login import current_user, login_user, logout_user
from portfolio.forms import LoginForm
from portfolio.models import Languages, Content, Users, Projects
import readtime
from datetime import datetime
from babel.dates import format_date, format_datetime, format_time
from babel.dates import get_month_names
import traceback

portfolio.app_context().push()


@portfolio.errorhandler(404)
def page_not_found(e):
    lang = request.lang
    proj_n = request.proj_n

    value = Content.get_value('', lang, '404_error')
    error400 = '' if not value else str(value['value'])
    value = Content.get_value('', lang, 'back_home')
    back_home = '' if not value else str(value['value'])

    return render_template('404.html', error400=error400, back_home=back_home,
                           lang=lang, proj_n=proj_n), 404


@portfolio.errorhandler(Exception)
def handle_all_errors(e):
    traceback.print_exc()
    response = {
        "error": str(e),
        "message": "An unexpected error occurred."
    }

    lang = request.lang
    proj_n = request.proj_n

    value = Content.get_value('', lang, 'error')
    error_text = '' if not value else str(value['value'])
    value = Content.get_value('', lang, 'error_subtitle')
    error_subtitle = '' if not value else str(value['value'])
    value = Content.get_value('', lang, 'back_home')
    back_home = '' if not value else str(value['value'])

    return render_template('error.html', error_text=error_text,
                           error_subtitle=error_subtitle, back_home=back_home,
                           lang=lang, proj_n=proj_n), 500

# Managing the context processor with multilanguage and title slugs for projects


@portfolio.before_request
def set_lang(lang=None):
    request.lang = request.args.get('lang', lang)


@portfolio.before_request
def set_proj(proj_n=1):
    """Since when the user can change the language, the webpage should to be the
    same, I need to save a reference to the exact line for the language that
    was changed, the id is different for every row (so if the user change the
    language, cannot find the same id for different language), the title_slug
    could change if the user wants to translate the titles, so I will use the
    project_n with the date to define the project that needs to translate

    Keyword arguments:
    date date of the project
    proj_n number of the project inside the date

    """

    request.proj_n = request.args.get('proj_n', proj_n)


@portfolio.before_request
def set_date(proj_date=None):
    request.proj_date = request.args.get('proj_date', proj_date)


@portfolio.before_request
def set_slug(slug=None):
    request.title_slug = request.args.get('title_slug', slug)


@portfolio.context_processor
def inject_data():
    lang = request.lang
    proj_n = request.proj_n
    proj_date = request.proj_date
    title_slug = request.title_slug

    languages = list([str(l) for l in Languages.get_all()])

    menu_home = menu_about = menu_contact = menu_projects = menu_manage = \
        menu_manage_home = menu_manage_about = menu_manage_projects = \
        menu_manage_contact = menu_manage_logout = foot = search_hint = ''

    try:
        value = Content.get_value('', lang, 'menu_home')
        menu_home = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_about')
        menu_about = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_contact')
        menu_contact = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_projects')
        menu_projects = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_manage')
        menu_manage = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_manage_home')
        menu_manage_home = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_manage_about')
        menu_manage_about = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_manage_projects')
        menu_manage_projects = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_manage_contact')
        menu_manage_contact = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'menu_manage_logout')
        menu_manage_logout = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'foot')
        foot = '' if not value else str(value['value'])

        value = Content.get_value('', lang, 'search')
        search_hint = '' if not value else str(value['value'])

    except KeyError as k:
        abort(500, k)

    return dict(languages=languages,
                menu_home=menu_home, menu_about=menu_about,
                menu_contact=menu_contact, menu_projects=menu_projects,
                menu_manage=menu_manage, menu_manage_home=menu_manage_home,
                menu_manage_about=menu_manage_about,
                menu_manage_projects=menu_manage_projects,
                menu_manage_contact=menu_manage_contact,
                menu_manage_logout=menu_manage_logout, foot=foot,
                proj_n=proj_n, proj_date=proj_date, title_slug=title_slug,
                search_hint=search_hint)

# Functions


def replace_image_tags(text, img_n, image):
    '''
    Function to replace the string <img>image(n)</img> with the html needed
    to render the images in a responsive way

    text: the text where need to replace
    img_n: the number of image to replace (image1, image2 or image3)
    image: the name of the image

    return modified_text: the text ready to render
    '''

    replacement_html = f'''<img loading="lazy" decoding="async" 
                        src="{ url_for('static', filename='img/projects/') }{ image }_1110.jpg" 
                        srcset="{ url_for('static', filename='img/projects/') }{ image }_545x.webp 545w,
                                { url_for('static', filename='img/projects/') }{ image }_600x.webp 600w,
                                { url_for('static', filename='img/projects/') }{ image }_700x.webp 700w,
                                { url_for('static', filename='img/projects/') }{ image }_1110x.webp 1110w"
                        sizes="(max-width: 575px) 545px,
                                (max-width: 767px) 600px,
                                (max-width: 991px) 700px,
                                1110px"
                        class="w-100 card-img-top img-fluid" 
                        alt="{ image }" 
                        width="1200" 
                        height="800">'''

    modified_text = text.replace(f"<img>{img_n}</img>", replacement_html)
    return modified_text


def replace_link_tag(text, proj_link):
    links = [proj_link.link1, proj_link.link2, proj_link.link3,
             proj_link.link4, proj_link.link5]

    for i in range(5):
        text = text.replace(f"<lnk>link{i+1}</lnk>", links[i])

    return text


def get_date_name(language, date):
    """"Function to get the name of the month in the selected language

    Keyword arguments:
    language -- iso code
    date 
    Return: the date
    """

    date_ojb = datetime.strptime(str(date), '%Y-%m-%d')
    day = date_ojb.day
    month_number = date_ojb.month
    year = date_ojb.year

    return f"{get_month_names(locale=language)[month_number]} {day}, {year}"


def get_lang_name_proj(proj_id):
    langid = Projects.query.filter_by(id=proj_id).first().languageid
    return Languages.query.filter_by(id=langid).first().language

# Views


@portfolio.route('/<path:path>')
def catch_all(path, lang):
    if lang is None:
        lang = 'en'

    print(f"***Non-existent route requested: {path}")
    abort(404)

# index


@portfolio.route('/')
@portfolio.route('/index/')
@portfolio.route('/<lang>/index/')
def index(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    # value = Content.get_value('', lang, 'menu_home')
    #    menu_home = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'get_touch')
    get_touch = '' if not value else str(value['value'])

    value = Content.get_value('index', lang, 'hello')
    hello = '' if not value else str(value['value'])

    value = Content.get_value('index', lang, 'name')
    name = '' if not value else str(value['value'])

    value = Content.get_value('index', lang, 'subtitle')
    subtitle = '' if not value else str(value['value'])

    return render_template('index.html', lang=lang, hello=hello, name=name,
                           subtitle=subtitle, get_touch=get_touch)

# about


@portfolio.route('/about/')
@portfolio.route('/<lang>/about/')
def about(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    value = Content.get_value('about', lang, 'hello')
    hello = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'parragraph1')
    parragraph1 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'parragraph2')
    parragraph2 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'parragraph3')
    parragraph3 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'parragraph4')
    parragraph4 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'parragraph5')
    parragraph5 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'parragraph6')
    parragraph6 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'skills_title')
    skills_title = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'skill1')
    skill1 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'skill2')
    skill2 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'skill3')
    skill3 = '' if not value else str(value['value'])

    value = Content.get_value('about', lang, 'youtube')
    youtube = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'more')
    more = '' if not value else str(value['value'])

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
def projects(lang=None, proj_date=None, proj_n=None, title_slug=None,
             keyw=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    langid = Languages.getid(lang)

    # Keywords
    query_keyw = request.args.get('q')
    all_keywords, keywords_freq = Projects.get_all_keyws_and_freq(langid,
                                                                  query_keyw)
    # Projects. Main template

    value = Content.get_value('', lang, 'keyw_title')
    keyw_title = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'search_keyw')
    key_search = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'more')
    more = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'previous')
    previous = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'next')
    next = '' if not value else str(value['value'])

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

    next_url = url_for('projects', lang=lang, keyw=keyw, proj_n=proj_n,
                       proj_date=proj_date, page=projs.next_num) \
        if projs.has_next else None

    prev_url = url_for('projects', lang=lang, proj_n=proj_n,
                       proj_date=proj_date, page=projs.prev_num) \
        if projs.has_prev else None

    return render_template('projects/index.html', lang=lang, projs=projs.items,
                           page=page, next_url=next_url, prev_url=prev_url,
                           more=more, previous=previous, next=next,
                           all_keywords=all_keywords,
                           keywords_freq=keywords_freq, keyw_title=keyw_title,
                           keyw=keyw, proj_n=proj_n, proj_date=proj_date,
                           get_date_name=get_date_name, key_search=key_search)


@portfolio.route('/project/<proj_date>/<proj_n>/<title_slug>/')
@portfolio.route('/<lang>/project/<proj_date>/<proj_n>/<title_slug>/')
def project(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    project = Projects.get_by_slug(Languages.getid(lang), title_slug)

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    value = Content.get_value('', lang, 'keyw_title')
    keyw_title = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'read')
    read = '' if not value else str(value['value'])

    time_reading = str(readtime.
                       of_markdown(" ".join(
                           [project.resume if project.resume else '',
                            project.exposition if project.exposition else '',
                            project.action if project.action else '',
                            project.resolution if project.resolution else '']))
                       ).replace('read', read)

    # Create the replacements for the images

    modified_text = replace_image_tags(project.resolution, 'image1',
                                       project.image1)
    modified_text = replace_image_tags(modified_text, 'image2',
                                       project.image2)
    modified_text = replace_image_tags(modified_text, 'image3',
                                       project.image3)

    modified_text = replace_link_tag(modified_text, project)

    return render_template('projects/project_detail.html', lang=lang,
                           proj_date=proj_date, proj_n=proj_n,
                           title_slug=title_slug, project=project,
                           keyw_title=keyw_title, time_reading=time_reading,
                           text=modified_text, get_date_name=get_date_name)


# contact

@portfolio.route('/contact/', methods=['GET', 'POST'])
@portfolio.route('/<lang>/contact/', methods=['GET', 'POST'])
def contact(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    value = Content.get_value('contact', lang, 'title')
    title = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'subtitle')
    subtitle = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'first_name')
    first_name = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'last_name')
    last_name = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'email')
    email = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'message')
    message = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'submit')
    submit = '' if not value else str(value['value'])

    value = Content.get_value('contact', lang, 'email_subject')
    email_subject = '' if not value else str(value['value'])

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

# search


@portfolio.route('/search/')
@portfolio.route('/<lang>/search/')
def search(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    query = request.args.get('q')

    if not query:
        return redirect(request.referrer)

    # Projects

    value = Content.get_value('', lang, 'more')
    more = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'previous')
    previous = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'next')
    next = '' if not value else str(value['value'])

    page = request.args.get('page', 1, type=int)

    projs, proj_total = Projects.search(query,
                                        page,
                                        portfolio.config['PROJECTS_PAGE'])

    next_url = url_for('search', q=query, page=page + 1) \
        if proj_total > page * portfolio.config['PROJECTS_PAGE'] else None

    prev_url = url_for('search', q=query, page=(page - 1)) \
        if page > 1 else None

    return render_template('search/index.html', lang=lang, projs=projs,
                           page=page, next_url=next_url, prev_url=prev_url,
                           more=more, previous=previous, next=next,
                           proj_n=proj_n, proj_date=proj_date,
                           get_date_name=get_date_name,
                           get_lang_name_proj=get_lang_name_proj)


# login


@portfolio.route(f"/{portfolio.config['PORTFOLIO_LOGIN_URL']}/",
                 methods=['GET', 'POST'])
@portfolio.route(f"/<lang>/{portfolio.config['PORTFOLIO_LOGIN_URL']}/",
                 methods=['GET', 'POST'])
def login(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    if current_user.is_authenticated:
        return redirect(url_for('index', lang=lang))

    form = LoginForm()

    value = Content.get_value('', lang, 'username')
    form.username.label.text = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'password')
    form.password.label.text = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'rememberme')
    form.remember_me.label.text = '' if not value else str(value['value'])

    value = Content.get_value('', lang, 'signin')
    form.submit.label.text = '' if not value else str(value['value'])

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            value = Content.get_value('', lang, 'errorlogin')
            flash('' if not value else value['value'])

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
def logout(lang=None, proj_date=None, proj_n=1, title_slug=None):
    if lang is None:
        lang = 'en'  # Set a default language if lang is not provided

    set_lang(lang)
    set_proj(proj_n)
    set_date(proj_date)
    set_slug(title_slug)

    logout_user()
    return redirect(url_for('index', lang=lang))

# manifest


@portfolio.route('/manifest.webmanifest')
def manifest():
    return send_from_directory('static', 'manifest.webmanifest')
