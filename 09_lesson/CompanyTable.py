from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:

  def __init__(self, connection_string):
    self.db = create_engine(connection_string)

  def get_companies(self):
    return self.db.execute("select * from company").fetchall()