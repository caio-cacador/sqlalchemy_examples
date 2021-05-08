from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_orm import HistoryDay, Acao

DB_USER = 'postgres'
DB_PASS = 'postgres'
IP = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME}')


Acao.__table__.create(bind=engine, checkfirst=True)
HistoryDay.__table__.create(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()