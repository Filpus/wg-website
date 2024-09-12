from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, Relationship

Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Culture(db.Model):
    __tablename__ = 'cultures'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    population = db.relationship('Pop',back_populates='cultures')
    countries = db.relationship('Country',back_populates='cultures')


class Religion(db.Model):
    __tablename__ = 'religions'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    population = db.relationship('Pop',back_populates='religions')
    countries = db.relationship('Country',back_populates='religions')

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    countries = db.relationship('Country',back_populates='players')
class Resource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    productionCost = db.Relationship('ProductionCost',back_populates='resources')
    magazine = db.relationship('Magazine',back_populates='resources')
    resourcesInLocalisation = db.relationship('ResourceInLocalisation',back_populates='resources')



class Country(db.Model):
    __tablename__ = 'countries'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    tax = db.Column(Float, default=0.0, nullable=False)
    gold = db.Column(Float, default=0.0, nullable=False)
    food = db.Column(Float, default=0.0, nullable=False)
    cultureId = db.Column(Integer, ForeignKey('cultures.id'), nullable=False)
    culture = db.relationship('Culture', back_populates='countries')
    religionId = db.Column(Integer, ForeignKey('religions.id'), nullable=False)
    relion = db.relationship('Religion', back_populates='countries')
    playerId = db.Column(Integer, ForeignKey('players.id'), nullable=False, unique=True)
    player = db.relationship('Player', back_populates='countries')
    localisations = db.relationship('Localisation', back_populates='countries')
    orderedProductions = db.relationship('OrderedProduction', back_populates='countries')
    accessToUnits = db.relationship('AccessToUnit', back_populates='countries')
    units = db.relationship('Unit', back_populates='countries')
    armies = db.relationship('Army', back_populates='countries')

class Localisation(db.Model):
    __tablename__ = 'localisations'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    localisationType = db.Column(String(50), nullable=False)
    fertility = db.Column(Float, default=0)
    wealth = db.Column(Float, default=0)
    size = db.Column(Integer, default=0)
    fortification = db.Column(Integer, default=0)
    country_id = db.Column(Integer, ForeignKey('countries.id'), default=0)
    country = db.relationship('Country', back_populates='localisations')
    population = db.relationship('Pop', back_populates='localisations')

class UnitType(db.Model):
    __tablename__ = 'unitType'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), unique=True, nullable=False)
    melee_attack = db.Column(Integer, default=0)
    ranged_attack = db.Column(Integer, default=0)
    speed = db.Column(Integer, default=0)
    morale = db.Column(Integer, default=0)
    manpower = db.Column(Integer, default=0)
    maintenance_cost = db.Column(Integer, default=0)
    land_or_naval = db.Column(Boolean, default=True)

    unit = db.relationship('Unit', back_populates='unitType')
    productionCost = db.relationship('ProductionCost', back_populates='unitType')
    accessToUnit = db.relationship('AccessToUnit', back_populates='unitType')



class AccessToUnit(db.Model):
    __tablename__ = 'accessToUnit'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)
    unitType_id = db.Column(Integer, ForeignKey('unitType.id'), nullable=False)

    unitType = db.relationship('UnitType', back_populates='accessToUnit')
    country = db.relationship('Country', back_populates='accessToUnit')


class ProductionCost(db.Model):
    __tablename__ = 'productionCost'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    unitType_id = db.Column(Integer, ForeignKey('unitType.id'), nullable=False)
    resource_id = db.Column(Integer, ForeignKey('resources.id'), nullable=False)
    cost = db.Column(Float, default=0, nullable=False)

    unitType = db.relationship('UnitType', back_populates='productionCost')
    resource = db.relationship('Resource', back_populates='productionCost')


class OrderedProduction(db.Model):
    __tablename__ = 'orderedProduction'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    productionCost_id = db.Column(Integer, ForeignKey('productionCost.id'), nullable=False)
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)
    number = db.Column(Integer, nullable=False)

    productionCost = db.relationship('ProductionCost', back_populates='orderedProduction')
    country = db.relationship('Country', back_populates='orderedProduction')


class ResourcesInLocalisation(db.Model):
    __tablename__ = 'resourcesInlocalisation'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    localisation_id = db.Column(Integer, ForeignKey('localisations.id'), nullable=False)
    resource_id =db.Column(Integer, ForeignKey('resources.id'), nullable=False)
    number = db.Column(Integer, nullable=False)

    localisation = db.relationship('Localisation', back_populates='resources')
    resource = db.relationship('Resource', back_populates='resources')

class Unit(db.Model):
    __tablename__ = 'units'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    unitType_id = db.Column(Integer, ForeignKey('unitType.id'), nullable=False)
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)
    number = db.Column(Integer, nullable=False)

    unitType = db.relationship('UnitType', back_populates='units')
    country = db.relationship('Country', back_populates='units')


class Army(db.Model):
    __tablename__ = 'armies'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), nullable=False)
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)
    localisation_id = db.Column(Integer, ForeignKey('localisations.id'), nullable=False)

    country = db.relationship('Country', back_populates='army')
    localisation = db.relationship('Localisation', back_populates='army')

class BelongsToArmy(db.Model):
    __tablename__ = 'belongsToArmy'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    army_id =db.Column(Integer, ForeignKey('armies.id'), nullable=False)
    unit_id = db.Column(Integer, ForeignKey('units.id'), nullable=False)

    army = db.relationship('Army', back_populates='belongsToArmy')
    unit = db.relationship('Unit', back_populates='belongsToArmy')



class Estate(db.Model):
    __tablename__ = 'estates'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(String(50), nullable=False)
    takingPartInIncome = db.Column(Float, default=0, nullable=False)
    takingPartInFood = db.Column(Float, default=0, nullable=False)
    manpower = db.Column(Float, default=0, nullable=False)
    baseHappiness = db.Column(Float, default=0, nullable=False)
    picture = db.Column(String(1000))

    population = db.Relationship('Pop', back_populates='estate')


class Pop(db.Model):
    __tablename__ = 'pops'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    culture_id = db.Column(Integer, ForeignKey('cultures.id'), nullable=False)
    estate_id = db.Column(Integer, ForeignKey('estates.id'), nullable=False)
    religion_id = db.Column(Integer, ForeignKey('religions.id'), nullable=False)
    localisation_id = db.Column(Integer, ForeignKey('localisations.id'), nullable=False)
    happiness = db.Column(Float, default=0.5, nullable=False)

    culture = db.relationship('Culture', back_populates='pop')
    estate = db.relationship('Estate', back_populates='pop')
    religion = db.relationship('Religion', back_populates='pop')
    localisation = db.relationship('Localisation', back_populates='pop')

class Action(db.Model):
    __tablename__ = 'actions'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    action = db.Column(String(1000))
    result = db.Column(String(1000))
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)

    country = db.relationship('Country', back_populates='action')


class Magazine(db.Model):
    __tablename__ = 'magazine'

    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)
    resource_id = db.Column(Integer, ForeignKey('resources.id'), nullable=False)
    number = db.Column(Integer, nullable=False, default=0)

    country = db.relationship('Country', back_populates='magazine')
    resource = db.relationship('Resource', back_populates='magazine')


class Modifier(db.Model):
    __tablename__ = 'modifiers'

    id =db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(50))
    description = db.Column(String(1000))

    effects = db.relationship('Effect', back_populates='modifier')
    appliesToCountry = db.relationship('AppliesToCountry', back_populates='modifier')


class Effect(db.Model):
    __tablename__ = 'effects'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    conditions = db.Column(String(1000), nullable=False)
    target = db.Column(String(1000), nullable=False)
    isPercentage = db.Column(Boolean, default=False, nullable=False)
    value = db.Column(Float, nullable=False)
    modifier_id = db.Column(Integer, ForeignKey('modifiers.id'), nullable=False)

    modifier = db.relationship('Modifier', back_populates='effects')


class AppliesToCountry(db.Model):
    __tablename__ = 'appliesToCountry'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(Integer, ForeignKey('countries.id'), nullable=False)
    modifier_id = db.Column(Integer, ForeignKey('modifiers.id'), nullable=False)

    country = db.relationship('Country', back_populates='appliesToCountry')
    modifier = db.relationship('Modifier', back_populates='appliesToCountry')


# Przykładowa funkcja do tworzenia bazy danych
def createPatronsDataBase(numberOfGame: int):
    gameCode = f'sqlite:///{numberOfGame}.db'
    engine = create_engine(gameCode, echo=True)
    Base.metadata.create_all(engine)