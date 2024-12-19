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
  
  def insert_card_manually(self, card):
    db_connection = self.get_connection()
    cursor = db_connection.cursor()

    query = f"INSERT INTO cards (name, description, card_type) VALUES (?, ?, ?)"
    card_data = (card.name, card.description, card.card_type)
    
    cursor.execute(query, card_data)
    db_connection.commit()
    
    cursor.close()
    db_connection.close()
    
#db = DatabaseManager()
#new_card = ("el pepe", "destruye todo el campo", "magica")
#db.insert_card_manually(new_card)
#cards = db.get_table_data("cards")
#print(cards)