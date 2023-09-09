from portfolio import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from collections import Counter

class Users(UserMixin, db.Model):
    _tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_user(self, uname):
        return Users.query.filter_by(username=uname).first()
    
    def get_all():
        return Users.query.all()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password_hash,            
            'email': self.email
        }

class Languages(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(2), index=True, unique=True)

    def __repr__(self):
        #return '<Language {}>'.format(self.language)
        return self.language.lower()

    def get_all():
        return Languages.query.all()
    
    def upper(self):
        return self.language.upper()
    
    def getid(lang):
        return Languages.query.filter(Languages.language == lang).first().id
    
class Content(db.Model):
    __tablename__ = 'portfolio_content'

    id = db.Column(db.Integer, primary_key=True)
    template = db.Column(db.String(20), index=True)
    variable = db.Column(db.String(20), index=True)
    languageid = db.Column(db.Integer, db.ForeignKey('languages.id', name='fk_languageid'))
    value = db.Column(db.String(250))    

    def __repr__(self):
        return '<Content {} {} {} {}>'.format(self.template, self.variable, self.languageid, self.value)
    
    def get_value(tem, lang, var) -> dict:
        if lang is None:
            return dict()
        
        langid = Languages.query.filter(Languages.language == lang).first().id

        cont = Content.query.filter(Content.template == str(tem or ''), Content.languageid == langid, 
                                    Content.variable == var).first()
        if cont:
            d = dict()
            d['value'] = cont.value
        return d

class Projects(db.Model):
    __tablename__ = 'portfolio_projects'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    project_n = db.Column(db.Integer) # This colum is the project number within the date
    languageid = db.Column(db.Integer, db.ForeignKey('languages.id', name='fk_languageid'))
    title = db.Column(db.String(50), index=True)
    resume = db.Column(db.String(250), index=True)    
    description = db.Column(db.String())   
    resolution = db.Column(db.String())
    keywords = db.Column(db.String(250), index=True)
    link1 = db.Column(db.String(250))
    link2 = db.Column(db.String(250))
    link3 = db.Column(db.String(250))
    link4 = db.Column(db.String(250))
    link5 = db.Column(db.String(250))
    image1 = db.Column(db.String(50))
    image2 = db.Column(db.String(50))
    image3 = db.Column(db.String(50))

    def __repr__(self):
        return '<Project {} {} {} {}>'.format(self.date, self.languageid, self.title, self.resume)
    
    def get_all():
        return Projects.query.all()
    
    def get_all_keyws_and_freq(langid):
        """This function will get all the keywords of the projects
        and will calculate their frequencies
        
        Keyword arguments:
        
        Return: one tuple with the distinct keywords and one dictionary with the frequencies
        """
        
        all_keyw = [tp.strip() for tuples in Projects.query
                    .filter(Projects.languageid == langid)
                    .with_entities(Projects.keywords).all() for tp in tuples[0].split(',')]

        keyws = sorted(tuple(set(all_keyw)))

        keyws_freq = dict(Counter(all_keyw))        

        return keyws, keyws_freq
@login.user_loader
def load_user(id):
    return Users.query.get(int(id))