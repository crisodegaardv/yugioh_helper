import sqlite3

class DatabaseManager:
  _connection = None
  
  def __init__(self, db_name="yugioh_helper"):
    """Initialize db connection."""
    if not DatabaseManager._connection:
      DatabaseManager._connection = sqlite3.connect(db_name)
      self.cursor = DatabaseManager._connection.cursor()
    else:
        self.cursor = DatabaseManager._connection.cursor()
    
  def get_table_data(self, table_name, condition="1=1"):
    query = f"SELECT * FROM {table_name} WHERE {condition}"
    self.cursor.execute(query)
    return self.cursor.fetchall()
  
  def insert(self, table_name, columns, values):
    placeholders = ", ".join("?" * len(values))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    self.cursor.execute(query, values)
    self.connection.commit()
    
  def get_cards(self, condition="1=1"):
    query = f"SELECT * FROM cards WHERE {condition}"
    self.cursor.execute(query)
    return self.cursor.fetchall()
    
  
  @classmethod
  def close(cls):
    if cls._connection:
      cls._connection.close()
      cls._connection = None