import sqlite3

class DatabaseManager:
  _db_name = "yugioh_helper"
  
  def __init__(self):
    pass
   
  @classmethod  
  def get_connection(cls):
    return sqlite3.connect(cls._db_name)
      
  def get_table_data(self, table_name):
    db_connection = self.get_connection()
    cursor = db_connection.cursor()

    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    
    cursor.close()
    db_connection.close()
    
    return result
  
  def insert_card_manually(self):
    db_connection = self.get_connection()
    

