from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)  # Добавьте для отладки
    assert names[-1] == 'app_users'

def test_select():
    inspector = inspect(db)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[-1]

def test_select_1_row():
    inspector = inspect(db)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 50).fetchall()

def test_select_1_row_with_two_filters():
    inspector = inspect(db)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id >= :id")

    my_params = {
        'id' : 10,
        'isActive' : True
    }

    rows = db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 2

def test_insert():
    inspector = inspect(db)
    sql = text("insert into company (\"name\") values (:new_name)")

    rows = db.execute(sql, new_name = 'SkyPro')

def test_update():
    inspector = inspect(db)
    sql = text("update company set description = :descr where id = :id")
    db.execute(sql, descr = 'New descr', id = 50)

def test_delete():
    inspector = inspect(db)
    sql = text("delete from company where id = :id")
    db.execute(sql, id = 50)