from portfolio import portfolio, db
from portfolio.models import Users

def create_user():
    u=Users(username='roque', email='roqueourense@gmail.com')
    u.set_password('roquisimo')
    db.session.add(u)
    db.session.commit()

if __name__ == '__main__':
    portfolio.app_context().push()  
    create_user()