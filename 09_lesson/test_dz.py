from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text
from sqlalchemy.orm import Session


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


# находим список всех таблиц
def test_get_info():
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)


# находим таблицу company
def test_get_table_company():
    with db.connect() as connection:
        # Используем text() для SQL запросов
        result = connection.execute(text("SELECT * FROM company"))
        rows = result.fetchall()
        print("Таблица company:", rows)


# добавляем данные в таблицу
def test_add_company():
    sql = text("INSERT INTO company (id, is_active, name, description) VALUES (:id, :is_active, :name, :description)")
    company_data = {
        'id': 201,
        'is_active': True,
        'name': 'Новая компания',
        'description': 'Тестовое описание компании'
    }

    try:
        with Session(db) as session:
            session.execute(sql, company_data)
            session.commit()
        print("Компания успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении компании: {e}")


# редактируем данные в таблице
def test_update_company():
    sql = text("UPDATE company SET name = :new_name, description = :new_description WHERE id = :id")
    update_data = {
        'id': 201,
        'new_name': 'Обновленное название',
        'new_description': 'Новое описание компании'
    }

    try:
        with Session(db) as session:
            session.execute(sql, update_data)
            session.commit()
        print("Данные компании успешно обновлены!")
    except Exception as e:
        print(f"Ошибка при обновлении компании: {e}")


# удаляем данные из таблицы
def test_delete_company():
    sql = text("DELETE FROM company WHERE id = :id")
    delete_data = {
        'id': 201
    }

    try:
        with Session(db) as session:
            session.execute(sql, delete_data)
            session.commit()
        print("Компания успешно удалена!")
    except Exception as e:
        print(f"Ошибка при удалении компании: {e}")


# Теперь запускаем тесты последовательно
if __name__ == "__main__":
    test_get_info()
    test_get_table_company()
    test_add_company()
    test_update_company()
    test_delete_company()
