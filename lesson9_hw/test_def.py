from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text
from sqlalchemy.orm import Session


db_connection_string = "postgresql://postgres:123456@localhost:5432/postgres"
db = create_engine(db_connection_string)


# находим список всех таблиц
def test_get_info():
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)
    assert names == ['subject']


# находим таблицу company
def test_get_table_company():
    with db.connect() as connection:
        # Используем text() для SQL запросов
        result = connection.execute(text("SELECT * FROM subject"))
        rows = result.fetchall()
        print("Таблица company:", rows)
        assert len(rows) > 0, "В таблице нет записей"


# добавляем данные в таблицу
def test_add_company():
    sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:subject_id , :subject_title)")
    company_data = {
        'subject_id': 10,
        'subject_title': 'Новая запись'
    }

    try:
        with Session(db) as session:
            result = session.execute(sql, company_data)
            session.commit()
            # Проверяем количество добавленных строк
            assert result.rowcount == 1, "Не удалось добавить запись"
        print("Компания успешно добавлена!")
    except Exception as e:
        print(f"Ошибка при добавлении компании: {e}")


# редактируем данные в таблице
def test_update_company():
    sql = text("UPDATE subject SET subject_title = :subject_title WHERE subject_id = :subject_id")
    update_data = {
        'subject_id': 10,
        'subject_title': 'Обновленное название'
    }

    try:
        with Session(db) as session:
            result = session.execute(sql, update_data)
            session.commit()
            # Проверяем количество обновленных строк
            assert result.rowcount == 1, "Не обновлена ни одна запись"
        print("Данные компании успешно обновлены!")
    except Exception as e:
        print(f"Ошибка при обновлении компании: {e}")


# удаляем данные из таблицы
def test_delete_company():
    sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
    delete_data = {
        'subject_id': 10
    }

    try:
        with Session(db) as session:
            result = session.execute(sql, delete_data)
            session.commit()
            # Проверяем количество удаленных строк
            assert result.rowcount == 1, "Не удалена ни одна запись"
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
