from sqlalchemy import create_engine, inspect

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)  # Добавьте для отладки
    assert names[-1] == 'app_users'

# Запуск теста
if __name__ == "__main__":
    test_db_connection()
    print("Тест пройден успешно!")


# from sqlalchemy import create_engine 


# db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

# def test_db_connection():
#     db = create_engine(db_connection_string)
#     names = db.table_names()
#     assert names[0] == 'company'