from sqlalchemy import *

from DataBases.Patrons.declarePatronsBase import createPatronsDataBase


def createMainDataBase():
    engine = create_engine('sqlite:///mainData.db', echo=True)
    meta = MetaData()
    users = Table('users', meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(50),unique=True),
                  Column('email', String(50),unique=True),
                  Column('password', String(50)))

    games = Table('games', meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(50), unique=True),
                  Column('nrOfDatabase', Integer), unique=True)
    rigthTable = Table('rigthTable', meta,
                       Column('id', Integer, primary_key=True),
                       Column('user',Integer,ForeignKey('users.id')),
                       Column('game',Integer,ForeignKey('games.id')))
    meta.create_all(engine)

def createGameBaseData(type:func,num:int):
    type(num)
if __name__ == '__main__':
    createGameBaseData(createPatronsDataBase, 2)