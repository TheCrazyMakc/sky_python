from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

# находим список всех таблиц
def test_get_info():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)

test_get_info()

# находим таблицу company
def test_get_table_company():
    inspector = inspect(db)
    rows = db.execute("select * from company").fetchall()
    print("Таблица company:", rows)

test_get_table_company()

def test_add_company():
    # SQL запрос для вставки данных
    sql = text("INSERT INTO company (id, is_active, name, description) VALUES (:id, :is_active, :name, :description)")

    # Данные для вставки
    company_data = {
        'id': 201,
        'is_active': True,
        'name': 'Новая компания',
        'description': 'Тестовое описание компании'
    }

    # Выполняем запрос
    with db.connect() as connection:
        result = connection.execute(sql, company_data)
        connection.commit()

    print("Компания успешно добавлена!")

test_add_company()

def test_update_company():
    # SQL запрос для обновления данных
    sql = text("UPDATE company SET name = :new_name, description = :new_description WHERE id = :id")

    # Данные для обновления
    update_data = {
        'id': 201,
        'new_name': 'Обновленное название',
        'new_description': 'Новое описание компании'
    }

    # Выполняем запрос
    with db.connect() as connection:
        result = connection.execute(sql, update_data)
        connection.commit()

    print("Данные компании успешно обновлены!")

test_update_company()

def test_delete_company():
    # SQL запрос для удаления
    sql = text("DELETE FROM company WHERE id = :id")

    # ID компании для удаления
    delete_data = {
        'id': 201
    }

    # Выполняем запрос
    with db.connect() as connection:
        result = connection.execute(sql, delete_data)
        connection.commit()

    print("Компания успешно удалена!")

test_delete_company()