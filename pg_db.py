import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Pg_db_manager:
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
    
  #def show_connection_data(self):
    #print(f"Connection data - db name: {self.dbname}, host: {self.host}, user: {self.user}, password: {self.password}, port: {self.port}")
  
pg_connection = Pg_db_manager()
#print(pg_connection.config)
query = "SELECT * FROM card_type"
results = pg_connection.execute_query(query, fetch=True)
print(results)
#pg_connection.show_connection_data()