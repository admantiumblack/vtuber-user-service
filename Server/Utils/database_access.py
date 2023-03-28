from Server.Config import get_db_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import lru_cache

class DBConfig():
    
    def __init__(self, url, autocommit=True, autoflush=True):
        self.engine = create_engine(url)
        self.local_sesion = sessionmaker(autocommit=autocommit, autoflush=autoflush, bind=self.engine)
    
    def get_connection(self):
        return self.local_sesion

@lru_cache
def get_session_maker(db_url:str=None):
    if db_url is None:
        settings = get_db_settings()
        db_url = settings.db_url
        
    return DBConfig(db_url)

def create_session(db_url=None):
    db_config = get_session_maker(db_url)
    local_sesion = db_config.get_connection()
    con = local_sesion()
    try:
        yield con
    finally:
        con.close()
