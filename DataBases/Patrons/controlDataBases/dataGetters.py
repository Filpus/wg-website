from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from DataBases.Patrons.classBasePatron import *


def get_countries(db_name: str):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)

    # Tworzenie sesji
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Pobieranie wszystkich krajów
        countries = session.query(Country).all()
        if countries:
            return countries
        else:
            return []
    finally:
        session.close()

def get_player_country(db_name: str, player_name: str):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        player = session.query(Player).filter(Player.name == player_name).first()
        if player:
            return player.countries
        else:
            return []
    finally:
        session.close()

def get_cultures(db_name: str):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        cultures = session.query(Culture).all()
        if cultures:
            return cultures
        else:
            return []
    finally:
        session.close()

def get_religions(db_name: str):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        religions = session.query(Religion).all()
        if religions:
            return religions
        else:
            return []
    finally:
        session.close()


def get_localisations_in_country(db_name: str, country: str):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        country = session.query(Country).filter(Country.name == country).first()
        if country:
            return country.localisations
        else:
            return []
    finally:
        session.close()

def get_population_of_country(db_name: str, country: str):
    localisations = get_localisations_in_country(db_name, country)

    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        populations = []
        for localisation in localisations:
            populations = populations + localisation.populations
        return populations
    finally:
        session.close()

