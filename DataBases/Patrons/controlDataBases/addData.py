from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


def add_row_to_table(db_name, table_name, table, **kwargs):
    # Tworzenie silnika połączenia z bazą danych
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=True)

    # Inicjalizacja metadanych
    meta = MetaData()
    meta.reflect(bind=engine)

    # Pobranie referencji do tabeli
    table = meta.tables.get(table_name)
    if not table:
        print(f"Table {table_name} does not exist.")
        return

    # Tworzenie sesji
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Dodanie nowego wiersza do tabeli
        insert_stmt = table.insert().values(**kwargs)
        session.execute(insert_stmt)
        session.commit()
        print(f"Added row to {table_name} table.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()


# Przykład użycia:
# Dodanie nowego wiersza do tabeli 'countries'
add_row_to_table(
    db_name='2',
    table_name='countries',
    name='Poland',
    tax=10.0,
    gold=100.0,
    food=50.0
)