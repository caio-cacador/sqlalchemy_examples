from sqlalchemy import Column, Integer, Numeric, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *

Base = declarative_base()
class PointsOfInterest(Base):
    __tablename__ = "points_of_interest"
    poi_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)


class Acao(Base):
    __tablename__ = 'acao'
    acao_id = Column(Integer, Sequence('acao_id_seq'), primary_key=True)
    acao_name = Column(String)


class HistoryDay(Base):
    __tablename__ = "history_day"
    __table_args__ = (
        PrimaryKeyConstraint('acao_id'),
    )
    history_id = Column(Integer, Sequence('history_day_id_seq'), primary_key=True)
    acao_id = Column(Integer, ForeignKey('acao.acao_id'))
    price_id = Column(Numeric)
    variation_id = Column(Numeric)
