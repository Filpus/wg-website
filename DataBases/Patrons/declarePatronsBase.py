from sqlalchemy import *

def createPatronsDataBase(numberOfGame: int):
    gameCode = 'sqlite:///' +  str(numberOfGame) + '.db'
    engine = create_engine(gameCode, echo=True)
    meta = MetaData()

    cultures = Table('cultures', meta,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(50), unique=True))
    religions = Table('religions', meta,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(50), unique=True))

    resources = Table('resources', meta,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(50), unique=True))
    countries = Table('countries', meta,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(50), unique=True),
                      Column('tax', Float, default=0.0),
                      Column('gold', Float, default=0.0),
                      Column('food', Float, default=0.0),)
    localisations = Table('localisations', meta,
                          Column('id', Integer, primary_key=True),
                          Column('name', String(50), unique=True),
                          Column('localisationType', String(50)),
                          Column('fertility', Float, default=0),
                          Column('wealth', Float, default=0),
                          Column('size',Integer, default=0),
                          Column('fortification',Integer,default=0),
                          Column('countries', Integer,ForeignKey('countries.id'), default=0, ))
    unitType = Table('unitType', meta,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(50), unique=True),
                     Column('melee_attack', Integer, default=0),
                     Column('ranged_attack', Integer, default=0),
                     Column('speed', Integer, default=0),
                     Column('morale', Integer, default=0),
                     Column('manpower', Integer, default=0),
                     Column('maintenance_cost', Integer, default=0),
                     Column('land_or_naval', Boolean, default=True),
                     )
    accessToUnit = Table('accessToUnit', meta,
                         Column('id', Integer, primary_key=True),
                         Column('country',Integer,ForeignKey('countries.id')),
                         Column('unitType',Integer,ForeignKey('unitType.id')),)
    productionCost = Table('productionCost', meta,
                           Column('id', Integer, primary_key=True),
                           Column('unitType',Integer,ForeignKey('unitType.id')),
                           Column('resource',Integer,ForeignKey('resources.id')),
                           Column('cost', Float, default=0),)
    orderedProduction = Table('orderedProduction', meta,
                              Column('id', Integer, primary_key=True),
                              Column('orderedProduction',Integer,ForeignKey('productionCost.id')),
                              Column('country',Integer,ForeignKey('countries.id')),
                              Column('number', Integer))
    resourcesInLocalisation = Table('resourcesInlocalisation', meta,
                                    Column('id', Integer, primary_key=True),
                                    Column('localisation',Integer,ForeignKey('localisations.id')),
                                    Column('resource',Integer,ForeignKey('resources.id')),
                                    Column('number',Integer))
    units = Table('units', meta,
                   Column('id', Integer, primary_key=True),
                   Column('unitType',Integer,ForeignKey('unitType.id')),
                  Column('country',Integer,ForeignKey('countries.id')),
                  Column('number', Integer))
    armies = Table('armies', meta,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(50)),
                   Column('country', Integer,ForeignKey('countries.id')),
                   Column('localisation',Integer,ForeignKey('localisations.id')))
    belongsToArmy = Table('belongsToArmy', meta,
                          Column('id', Integer, primary_key=True),
                          Column('armies',Integer,ForeignKey('armies.id')),
                          Column('unitType',Integer,ForeignKey('unitType.id')))
    estates = Table('estates', meta,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('takingPartInIncome',Float,default=0),
                    Column('takingPartInFood',Float,default=0),
                    Column('manpower',Float,default=0),
                    Column('baseHappiness',Float,default=0))
    pops = Table('pops', meta,
                 Column('id', Integer, primary_key=True),
                 Column('culture',Integer,ForeignKey('cultures.id')),
                 Column('estate',Integer,ForeignKey('estates.id')),
                 Column('religion',Integer,ForeignKey('religions.id')),
                 Column('localisation',Integer,ForeignKey('localisations.id')),
                 Column('happiness',Float,default=0.5))
    actions = Table('actions', meta,
                    Column('id', Integer, primary_key=True),
                    Column('action', String(1000)),
                    Column('result',String(1000)),
                    Column('country',Integer,ForeignKey('countries.id')))
    magazine = Table('magazine', meta,
                     Column('id', Integer, primary_key=True),
                     Column('country',Integer,ForeignKey('countries.id')),
                     Column('resource',Integer,ForeignKey('resources.id')),
                     Column('number',Integer))
    modifiers = Table('modifiers', meta,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(50)),
                      Column('describe',String(1000)))
    effects = Table('effects', meta,
                    Column('id', Integer, primary_key=True),
                    Column('conditions', String(1000)),
                    Column('target', String(1000)),
                    Column('isPercentage',Boolean,default=False),
                    Column('value',Float),
                    Column('modifiers',Integer,ForeignKey('modifiers.id')))
    appliesToCountry = Table('appliesToCountry', meta,
                             Column('id', Integer, primary_key=True),
                             Column('country',Integer,ForeignKey('countries.id')),
                             Column('modifiers',Integer,ForeignKey('modifiers.id')))
    meta.create_all(engine)