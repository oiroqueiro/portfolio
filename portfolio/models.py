from portfolio import db

class Users(db.Model):
    _tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

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
    link = db.Column(db.String(150))    

    def __repr__(self):
        return '<Content {} {} {} {}>'.format(self.template, self.variable, self.languageid, self.value)
    
    def get_value(tem, lang, var) -> dict:
        langid = Languages.query.filter(Languages.language == lang).first().id
        cont = Content.query.filter(Content.template == tem, Content.languageid == langid, 
                                    Content.variable == var).first()
        if cont:
            d = dict()
            d['value'] = cont.value
            d['link'] = cont.link
        return d