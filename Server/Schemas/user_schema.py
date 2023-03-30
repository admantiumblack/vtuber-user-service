from pydantic import BaseModel, validator
from datetime import datetime
from fastapi import HTTPException
from typing import List

class GetUserSchema(BaseModel):
    vtuber_id:int = None
    limit: int = 5
    offset: int = 0
    company: str = None
    platform: str = None
    include:str = 'details'

class GetCompanySchema(BaseModel):
    company_name:str = None
    limit:int = 5
    offset:int = 0

class PlatformSchema(BaseModel):
    platform_name:str = None
    class Config:
        orm_mode=True

class ChannelSchema(BaseModel):
    channel_name:str = None
    platform:PlatformSchema = None
    class Config:
        orm_mode=True

class CompanySchema(BaseModel):
    company_name:str = None

    class Config:
        orm_mode=True

class VtuberCompanySchema(BaseModel):
    company:CompanySchema = None

    class Config:
        orm_mode=True

class UserSchema(BaseModel):
    vtuber_id:int = None
    vtuber_name:str = None
    channel:List[ChannelSchema] = None
    companies:List[VtuberCompanySchema] = None
    details:dict = None

    class Config:
        orm_mode=True