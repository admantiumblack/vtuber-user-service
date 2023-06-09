from fastapi import APIRouter, Depends, Request
from Server.Schemas.user_schema import GetUserSchema, UserSchema, GetCompanySchema, CompanySchema
from Server.Schemas.generic_schema import GenericResponse
from Server.Utils.database_access import create_session
from Server.Utils.url_utils import create_metadata
from Server.Models.models import Vtuber
from typing import List
from Server.Controller.user_controller import filter_vtuber, filter_company


user_routes = APIRouter(
    prefix='/user'
)


@user_routes.get('/list', status_code=201, response_model=GenericResponse[UserSchema])
def get_user_list_route(request:Request, user_query=Depends(GetUserSchema), db=Depends(create_session)):
    params = user_query.dict(exclude_none=True)
    res = filter_vtuber(db, **params)
    metadata = create_metadata(request.url._url.split('?')[0], **params)
    return {'data': res, 'metadata':metadata}

@user_routes.get('/company', status_code=201, response_model=GenericResponse[CompanySchema])
def get_companies(request:Request, company_query=Depends(GetCompanySchema),db=Depends(create_session)):
    params = company_query.dict(exclude_none=True)
    res = filter_company(db, **params)
    metadata = create_metadata(request.url._url.split('?')[0], **params)
    return {'data': res, 'metadata':metadata}