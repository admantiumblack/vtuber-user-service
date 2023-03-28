from pydantic import BaseSettings
from functools import lru_cache

class ServerSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000
    reload: bool = True

@lru_cache
def get_server_settings():
    return ServerSettings()