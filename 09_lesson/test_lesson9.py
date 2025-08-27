from sqlalchemy import create_engine, inspect


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


# def test_db_connection():
# # Используем инспектор для получения информации о таблицах
# 	inspector = inspect(db)
# 	names = inspector.get_table_names()
  
# def test_select():
#     # в переменную записываем все строки из таблицы по запросу
#     rows = db.execute("SELECT * FROM company").fetchall()
#     print(rows)
#     row1 = rows[0]

#     assert row1[0] == 1
#     assert row1["name"] == "QA Студия 'ТестировщикЪ'"

db1 = inspect(create_engine("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")).get_table_names()
print(db1)