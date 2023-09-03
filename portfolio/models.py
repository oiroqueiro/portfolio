from portfolio import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

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
        cont = Content.query.filter(Content.template == tem, Content.languageid == langid, 
                                    Content.variable == var).first()
        if cont:
            d = dict()
            d['value'] = cont.value
        return d

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))