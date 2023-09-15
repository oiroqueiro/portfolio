from portfolio import portfolio, db
from portfolio.models import Content, Projects

if __name__ == '__main__':
    portfolio.app_context().push()  
    
    Content.reindex()

    Projects.reindex()