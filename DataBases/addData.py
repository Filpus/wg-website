from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


def add_row_to_table(db_name, table_name, table, **kwargs):
    gameCode = f'sqlite:///{db_name}.db'
    engine = create_engine(gameCode, echo=True)

    meta = MetaData()
    meta.reflect(bind=engine)

    table = meta.tables.get(table_name)
    if not table:
        print(f"Table {table_name} does not exist.")
        return

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        insert_stmt = table.insert().values(**kwargs)
        session.execute(insert_stmt)
        session.commit()
        print(f"Added row to {table_name} table.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()


def add_row_to_db(db_number, table_model, **kwargs):
    engine = create_engine(f'sqlite:///{db_number}.db')

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_row = table_model(**kwargs)

        session.add(new_row)

        session.commit()
        print(f"Added {new_row} to {table_model.__tablename__} table.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()
