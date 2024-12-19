import os
import psycopg2
from dotenv import load_dotenv
from card import Card

load_dotenv()

class PgDbManager:
  def __init__(self):
    
    self.config = {
      "dbname": os.getenv("DB_NAME"),
      "user": os.getenv("DB_USER"),
      "password": os.getenv("DB_PASSWORD"),
      "host": os.getenv("DB_HOST"),
      "port": os.getenv("DB_PORT")
    }
    
  def execute_query(self, query, params=None, fetch=False):
    try:
      with psycopg2.connect(**self.config) as connection:
        with connection.cursor() as cursor:
          cursor.execute(query, params)
          if fetch: 
            return cursor.fetchall()
          connection.commit()
    except psycopg2.Error as e:
      print(f"Error executing the query: {e}")
      return None
          
  def get_cards_data(self):
    try:
      query = """
        SELECT c.id,
            c.name,
            c.description,
            ct.type
        FROM card AS c
        INNER JOIN card_type AS ct ON c.card_type_id = ct.id;
      """
      result = self.execute_query(query, fetch=True)
      return result
      
    except exception as ex:
      print(ex)
      
  def insert_card_manually(self, card: Card):
    try:
      card.card_type = card.card_type.lower()
      
      if card.card_type == "monster":
        card.card_type = 1
      elif card.card_type =="spell":
        card.card_type = 2
      elif card.card_type == "trap":
        card.card_type = 3
        
      card_values = (card.name, card.description, card.card_type)
              
      placeholders = ", ".join(["%s"] * (len(vars(card)) - 1))
      query = f"INSERT INTO card (name, description, card_type_id) VALUES ({placeholders})"

      self.execute_query(query, card_values)
    except Exception as ex:
      print(ex)
  
  def get_card_types(self):
    query = f"SELECT type FROM card_type"
    result = self.execute_query(query, fetch=True)
    cleaned_result = [row[0] for row in result]
    return cleaned_result
     
#db = PgDbManager()
#card_types = db.get_card_types()
#print(card_types) 
#card1 = Card("pilin afterburner", "kill the enemy", "trap")
#db.insert_card_manually(card1)
#print(db.get_card_data())
    
