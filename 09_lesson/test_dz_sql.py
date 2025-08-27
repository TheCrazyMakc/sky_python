from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

# находим список всех таблиц
def test_git_info():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)  # Добавьте для отладки

test_git_info()

# находим таблицу company
def test_get_table_company():
    inspector = inspect(db)
    rows = db.execute("select * from company").fetchall()
    print("Таблица company:", rows)

test_get_table_company()

# добавляем данные в таблицу company
