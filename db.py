import sqlite3

class DatabaseManager:
  def __init__(self, db_name):
    """Initialize db connection."""
    self.db_name = db_name
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
    
  def query(self, table_name, condition="1=1"):
    query = f"SELECT * FROM {table_name} WHERE {condition}"
    self.cursor.execute(query)
    return self.cursor.fetchall()
  
  def insert(self, table_name, columns, values):
    placeholders = ", ".join("?" * len(values))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    self.cursor.execute(query, values)
    self.connection.commit()
  
  def close(self):
    self.connection.close()