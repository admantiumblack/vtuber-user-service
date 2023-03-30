from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime

Base = declarative_base()

class BaseDatabaseModel(Base):
    __abstract__ = True

    @classmethod
    def get(cls, db, limit = None, offset = None, **kwargs):
        query = db.query(cls).filter_by(**kwargs)
        if limit:
            query = query.limit(limit)
        
        if offset:
            query = query.offset(offset)
        return query

class DateTimeModel(BaseDatabaseModel):
    __abstract__ = True
    begin_date = Column(DateTime, primary_key=False, index=False)
    end_date = Column(DateTime, primary_key=False, index=False)