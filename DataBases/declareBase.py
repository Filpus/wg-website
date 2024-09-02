from sqlalchemy import *

from DataBases.Patrons.declarePatronsBase import createPatronsDataBase


def createMainDataBase():
    engine = create_engine('sqlite:///mainData.db', echo=True)
    meta = MetaData()
    users = Table('users', meta,
                  Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                  Column('name', String(50),unique=True, nullable=False),
                  Column('email', String(50),unique=True, nullable=False),
                  Column('password', String(50)))

    games = Table('games', meta,
                  Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                  Column('name', String(50), unique=True, nullable=False),
                  Column('nrOfDatabase', Integer), unique=True, nullable=False)
    rigthTable = Table('rigthTable', meta,
                       Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                       Column('user',Integer,ForeignKey('users.id'), nullable=False),
                       Column('game',Integer,ForeignKey('games.id'), nullable=False))
    meta.create_all(engine)

def createGameBaseData(type:func,num:int):
    type(num)
if __name__ == '__main__':
    createGameBaseData(createPatronsDataBase, 2)