from Server.Models.models import Vtuber, Company, StreamPlatform, VtuberCompany, VtuberPlatform
from Server.Utils.web_access import get_api_response
from Server.Config import get_holodex_settings

def filter_vtuber(db, limit=5, offset=0, include='', **params):
    print(params)
    query = Vtuber.get_vtuber(db, limit, offset, **params)
    res = query.all()
    include = set(include.split(','))
    
    if 'details' in include:
        for i in res:
            id = i.channel[0].channel_id
            i.details = get_api_response(get_holodex_settings(), f'channels/{id}')
    return res