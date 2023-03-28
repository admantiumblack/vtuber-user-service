from Server.Config.base_config import ApiSettings
from functools import lru_cache

class HolodexSettings(ApiSettings):
    
    class Config:
        env_prefix = 'holodex_'
    
@lru_cache
def get_holodex_settings():
    return HolodexSettings()