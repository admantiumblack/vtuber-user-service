from Server.Models.models import Vtuber, Company, StreamPlatform, VtuberCompany, VtuberPlatform

def filter_vtuber(db, limit=5, offset=0, **params):
    print(params)
    query = Vtuber.get_vtuber(db, **params)
    return query.all()