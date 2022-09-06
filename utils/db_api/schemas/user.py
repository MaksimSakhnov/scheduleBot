import sqlalchemy
from sqlalchemy import Column, BigInteger, String

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    user_url = Column(String(60))
    query: sqlalchemy.select
