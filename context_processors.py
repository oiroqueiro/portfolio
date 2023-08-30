from portfolio.models import Content

def content_values(lang=None):
    menu_home = Content.get_value('',lang,'menu_home')['value']
    menu_about = Content.get_value('',lang,'menu_about')['value']
    menu_contact = Content.get_value('',lang,'menu_contact')['value']
    menu_projects = Content.get_value('',lang,'menu_projects')['value']
    get_touch = Content.get_value('',lang,'get_touch')['value']
    foot = Content.get_value('',lang,'foot')['value']

    return {
        'menu_home': menu_home,
        'menu_about': menu_about,
        'menu_contact': menu_contact,
        'menu_projects': menu_projects,
        'get_touch': get_touch,
        'foot': foot,
    }