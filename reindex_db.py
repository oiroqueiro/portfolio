from portfolio import portfolio, db
from portfolio.models import Projects

if __name__ == '__main__':
    portfolio.app_context().push()  
    
    

    Projects.reindex()