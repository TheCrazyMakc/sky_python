from sqlalchemy import create_engine, inspect
import pytest

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

# Фикстура для подключения к БД
@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(db_connection_string)
    yield engine
    engine.dispose()

# Тестовые функции
def test_db_connection(db_engine):
    """Тест подключения к базе данных"""
    with db_engine.connect() as connection:
        result = connection.execute("SELECT 1")
        assert result.scalar() == 1

def test_table_exists(db_engine):
    """Тест наличия таблицы app_users"""
    inspector = inspect(db_engine)
    names = inspector.get_table_names()
    print("Все таблицы в базе:", names)
    assert 'app_users' in names

def test_table_position(db_engine):
    """Тест позиции таблицы app_users"""
    inspector = inspect(db_engine)
    names = inspector.get_table_names()
    assert names[1] == 'app_users'

def test_multiple_tables(db_engine):
    """Тест наличия нескольких важных таблиц"""
    inspector = inspect(db_engine)
    names = inspector.get_table_names()
    expected_tables = ['company', 'app_users']
    for table in expected_tables:
        assert table in names, f"Таблица {table} не найдена"