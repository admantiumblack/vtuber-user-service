from Server.Utils.url_utils import build_url
from pydantic import BaseSettings

class ApiSettings(BaseSettings):
    host: str = ''
    secret_key: str = ''

    def build_url(self, path, **param):
        param_with_key = {
            'key': self.secret_key,
            **param
        }
        return build_url(self.host+'/'+path, **param_with_key)