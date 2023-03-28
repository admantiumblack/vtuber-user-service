from pydantic import BaseSettings
from functools import lru_cache

class DBSettings(BaseSettings):
    db_host: str = '127.0.0.1'
    db_port: int = 3306
    db_provider: str = 'mysql+mysqldb'
    db_name: str = ''
    db_user: str = None
    db_pass: str = None

    @property
    def db_url(self):
        return f'{self.db_provider}://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'

@lru_cache
def get_db_settings():
    return DBSettings()