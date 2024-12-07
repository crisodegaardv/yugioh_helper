import sys
from db import DatabaseManager
from termcolor import colored, cprint

class Menu:
  def __init__(self):
    self.database = DatabaseManager()
  
  def main_menu(self):
    while True:
      cprint("\nMain Menu:", "yellow")
      cprint("1. Check cards", "cyan")
      cprint("2. Check decks", "cyan")
      cprint("3. Check combos", "cyan")
      cprint("4. Insert card manually")
      cprint("5. Exit", "red")
      
      choice = input("Enter your choice: ")
      
      if choice == "1":
        self.get_cards()
      elif choice == "2":
        self.sub_menu_1()
      elif choice == "3":
        print("y este otro deah que le pasaba")
      elif choice == "4":
        self.insert_card_manually()
      elif choice == "5":
        break
      else:
        print("Invalid data, ponte vío")
  
  def sub_menu_1(self):
    while True:
      print("sub menu option 1")
      print("sub menu option 2")
      choice = input("elige una opción del sub menú")
      
      if choice == "1":
        print("seleccionaste la opción 1 del sub menú, mensaje kl malo xdd")
      elif choice == "2":
        print("volviste bb")
        break  
      else:
        print("opción invalida")
      
  def get_cards(self):
    cards = self.database.get_table_data("cards")
    if cards:
      for card in cards:
        print(f"\nID: {card[0]}, Name: {card[1]}, Description: {card[2]}")
    else: 
      print("No cards found")
      
  def insert_card_manually(self):
    card_name = input("Enter card name: ")
    card_description = input("Enter card description: ")
    card_type = input("Enter card type: ")
    
    card_data = (card_name, card_description, card_type)
    
    self.database.insert_card_manually(card_data)
    print("card has been added to the db")
    
