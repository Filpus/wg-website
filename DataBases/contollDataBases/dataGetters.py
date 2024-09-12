from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from DataBases.Patrons.classBasePatron import Player


def get_player(db_name: str, player_name: str):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        player = session.query(Player).filter(Player.name == player_name).first()
        if player:
            return player
        else:
            return []
    finally:
        session.close()


def get_player_password(db_name: str, player_name: str):
    player = get_player(db_name, player_name)
    if player:
        return player.password
    else:
        return []


def get_player_email(db_name: str, player_name: str):
    player = get_player(db_name, player_name)
    if player:
        return player.email
    else:
        return []