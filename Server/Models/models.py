from Server.Models.base_model import Base, DateTimeModel, BaseDatabaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

class Vtuber(BaseDatabaseModel):
    __tablename__ = 'vtuber'
    vtuber_id = Column(Integer, primary_key=True, index=True)
    vtuber_name = Column(String, primary_key=False, index=False)
    
    channel = relationship(
        "VtuberPlatform", 
        back_populates='owner',
        primaryjoin=f'and_(Vtuber.vtuber_id==VtuberPlatform.vtuber_id, VtuberPlatform.end_date=="{datetime(year=9999, month=12, day=31)}")'
    )
    companies = relationship(
        "VtuberCompany", 
        back_populates='vtuber',
        primaryjoin=f'and_(Vtuber.vtuber_id==VtuberCompany.vtuber_id, VtuberCompany.end_date=="{datetime(year=9999, month=12, day=31)}")'
    )

    @classmethod
    def get_vtuber(cls, db, limit=5, offset=0, company=None, platform=None, **params):
        query = db.query(Vtuber).filter_by(**params)

        if company:
            company_id = Company.get(db, company_name=company).first().company_id
            query = query.filter(Vtuber.companies.any(company_id=company_id))
    
        if platform:
            platform_id = StreamPlatform.get(db, platform).first().platform_id
            query = query.filter(Vtuber.channel.any(platform_id=platform_id))

        if limit:
            query = query.limit(limit)
        
        if offset:
            query = query.offset(offset)
        return query
        

class VtuberPlatform(DateTimeModel):
    __tablename__ = 'vtuber_platform'
    channel_id = Column(String, primary_key=True, index=True)
    vtuber_id = Column(Integer, ForeignKey("vtuber.vtuber_id"), primary_key=False, index=True)
    platform_id = Column(Integer, ForeignKey("stream_platform.platform_id"), primary_key=False, index=True)
    channel_name = Column(String, primary_key=False, index=False)

    owner = relationship("Vtuber", back_populates='channel')
    platform = relationship('StreamPlatform', back_populates='channel')

class StreamPlatform(BaseDatabaseModel):
    __tablename__ = 'stream_platform'
    platform_id = Column(Integer, primary_key=True, index=True)
    platform_name = Column(String, primary_key=False, index=False)

    channel = relationship('VtuberPlatform', back_populates='platform')

class Company(BaseDatabaseModel):
    __tablename__ = 'company'
    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, primary_key=False, index=False)

    employees = relationship(
        'VtuberCompany', 
        back_populates='company',
        primaryjoin=f'and_(Company.company_id==VtuberCompany.company_id, VtuberCompany.end_date=="{datetime(year=9999, month=12, day=31)}")'
    )

class VtuberCompany(DateTimeModel):
    __tablename__ = 'vtuber_company'
    vtuber_id = Column(Integer, ForeignKey("vtuber.vtuber_id"), primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.company_id"), primary_key=True, index=True)

    vtuber = relationship("Vtuber", back_populates='companies')
    company = relationship('Company', back_populates='employees')