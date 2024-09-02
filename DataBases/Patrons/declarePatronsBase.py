from sqlalchemy import *

def createPatronsDataBase(numberOfGame: int):
    gameCode = 'sqlite:///' +  str(numberOfGame) + '.db'
    engine = create_engine(gameCode, echo=True)
    meta = MetaData()

    cultures = Table('cultures', meta,
                     Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                     Column('name', String(50), unique=True, nullable=False))
    religions = Table('religions', meta,
                      Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                      Column('name', String(50), unique=True, nullable=False))

    resources = Table('resources', meta,
                      Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                      Column('name', String(50), unique=True, nullable=False))
    countries = Table('countries', meta,
                      Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                      Column('name', String(50), unique=True, nullable=False),
                      Column('tax', Float, default=0.0, nullable=False),
                      Column('gold', Float, default=0.0, nullable=False),
                      Column('food', Float, default=0.0, nullable=False))
    localisations = Table('localisations', meta,
                          Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                          Column('name', String(50), unique=True, nullable=False),
                          Column('localisationType', String(50), nullable=False),
                          Column('fertility', Float, default=0),
                          Column('wealth', Float, default=0),
                          Column('size',Integer, default=0),
                          Column('fortification',Integer,default=0),
                          Column('countries', Integer,ForeignKey('countries.id'), default=0, ))
    unitType = Table('unitType', meta,
                     Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                     Column('name', String(50), unique=True, nullable=False),
                     Column('melee_attack', Integer, default=0),
                     Column('ranged_attack', Integer, default=0),
                     Column('speed', Integer, default=0),
                     Column('morale', Integer, default=0),
                     Column('manpower', Integer, default=0),
                     Column('maintenance_cost', Integer, default=0),
                     Column('land_or_naval', Boolean, default=True),
                     )
    accessToUnit = Table('accessToUnit', meta,
                         Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                         Column('country',Integer,ForeignKey('countries.id'), nullable=False),
                         Column('unitType',Integer,ForeignKey('unitType.id'), nullable=False))
    productionCost = Table('productionCost', meta,
                           Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                           Column('unitType',Integer,ForeignKey('unitType.id'), nullable=False),
                           Column('resource',Integer,ForeignKey('resources.id'), nullable=False),
                           Column('cost', Float, default=0), nullable=False)
    orderedProduction = Table('orderedProduction', meta,
                              Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                              Column('orderedProduction',Integer,ForeignKey('productionCost.id'), nullable=False),
                              Column('country',Integer,ForeignKey('countries.id'), nullable=False),
                              Column('number', Integer), nullable=False)
    resourcesInLocalisation = Table('resourcesInlocalisation', meta,
                                    Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                                    Column('localisation',Integer,ForeignKey('localisations.id'), nullable=False),
                                    Column('resource',Integer,ForeignKey('resources.id'), nullable=False),
                                    Column('number',Integer), nullable=False)
    units = Table('units', meta,
                   Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                   Column('unitType',Integer,ForeignKey('unitType.id'), nullable=False),
                  Column('country',Integer,ForeignKey('countries.id'), nullable=False),
                  Column('number', Integer, nullable=False))
    armies = Table('armies', meta,
                   Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                   Column('name', String(50), nullable=False),
                   Column('country', Integer,ForeignKey('countries.id'), nullable=False),
                   Column('localisation',Integer,ForeignKey('localisations.id'), nullable=False))
    belongsToArmy = Table('belongsToArmy', meta,
                          Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                          Column('armies',Integer,ForeignKey('armies.id'), nullable=False),
                          Column('unitType',Integer,ForeignKey('unitType.id'), nullable=False))
    estates = Table('estates', meta,
                    Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                    Column('name', String(50), nullable=False),
                    Column('takingPartInIncome',Float,default=0, nullable=False),
                    Column('takingPartInFood',Float,default=0, nullable=False),
                    Column('manpower',Float,default=0, nullable=False),
                    Column('baseHappiness',Float,default=0, nullable=False))
    pops = Table('pops', meta,
                 Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                 Column('culture',Integer,ForeignKey('cultures.id'), nullable=False),
                 Column('estate',Integer,ForeignKey('estates.id'), nullable=False),
                 Column('religion',Integer,ForeignKey('religions.id'), nullable=False),
                 Column('localisation',Integer,ForeignKey('localisations.id'), nullable=False),
                 Column('happiness',Float,default=0.5, nullable=False))
    actions = Table('actions', meta,
                    Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                    Column('action', String(1000)),
                    Column('result',String(1000)),
                    Column('country',Integer,ForeignKey('countries.id'), nullable=False))
    magazine = Table('magazine', meta,
                     Column('id', Integer, primary_key=True,autoincrement=True, nullable=False),
                     Column('country',Integer,ForeignKey('countries.id'), nullable=False),
                     Column('resource',Integer,ForeignKey('resources.id'), nullable=False),
                     Column('number',Integer, nullable=False, default=0))
    modifiers = Table('modifiers', meta,
                      Column('id', Integer, primary_key=True,autoincrement=True),
                      Column('name', String(50)),
                      Column('describe',String(1000)))
    effects = Table('effects', meta,
                    Column('id', Integer, primary_key=True,autoincrement=True),
                    Column('conditions', String(1000), nullable=False),
                    Column('target', String(1000), nullable=False),
                    Column('isPercentage',Boolean,default=False, nullable=False),
                    Column('value',Float, nullable=False),
                    Column('modifiers',Integer,ForeignKey('modifiers.id'), nullable=False))
    appliesToCountry = Table('appliesToCountry', meta,
                             Column('id', Integer, primary_key=True,autoincrement=True),
                             Column('country',Integer,ForeignKey('countries.id'), nullable=False),
                             Column('modifiers',Integer,ForeignKey('modifiers.id'), nullable=False))
    meta.create_all(engine)