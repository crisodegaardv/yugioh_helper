from menu import Menu
from card import Card
from db import DatabaseManager

class CardApp:
  def __init__(self):
    self.database = DatabaseManager()
    self.table_name = "cards"
    #self.setup_database()
    
  def add_card(self, card):
    self.db.insert(
      self.table_name,
      "name, description, card_type",
      (
        card.name, 
        card.description, 
        card.card_type
      )
    )
    
  def show_all_cards(self):
    cards = self.db.query(self.table_name)
    for card in cards:
      print(f"Card ID: {card[0]}\nCard Name: {card[1]}\nDescription: {card[2]}\nType: {card[3]}\n")
 
  def close(self):
    self.database.close()

def main():
  menu = Menu()
  menu.main_menu()
    
if __name__ == "__main__":
  main()
  
  app = CardApp()
  
  card1 = Card(
    "Sky Striker Ace - Raye", 
    "(Quick Effect): You can Tribute this card; Special Summon 1 'Sky Striker Ace'.",
    "Monster"
  )
  
  card2 = Card(
    "Sky Striker Maneuver - Afterburners", 
    "If you control no monsters in your Main Monster Zones: Destroy 1 face-up monster on the field.",
    "Spell"
  )
  
  #app.add_card(card1)
  #app.add_card(card2)
  #print("All cards in the database:")
  #app.show_all_cards()
