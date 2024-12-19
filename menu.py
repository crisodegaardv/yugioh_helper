import sys
from db import DatabaseManager
from termcolor import colored, cprint
from pg_db import PgDbManager
from card import Card

class Menu:
  def __init__(self):
    self.database = DatabaseManager()
    self.pg_db = PgDbManager()
  
  def main_menu(self):
    while True:
      cprint("\nMain Menu:", "yellow")
      cprint("1. Card menu", "cyan")
      cprint("2. Check decks", "cyan")
      cprint("3. Check combos", "cyan")
      cprint("4. Exit", "red")
      
      choice = input("Enter your choice: ")
      
      if choice == "1":
        self.card_menu()
      elif choice == "2":
        self.sub_menu_1()
      elif choice == "3":
        print("y este otro deah que le pasaba")
      elif choice == "4":
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
      
  def card_menu(self):
    while True:
      cprint("\n Card Menu", "red")
      cprint("1. Show all cards")
      cprint("2. Insert card manually")
      cprint("3. Delete all cards")
      cprint("4. Volver")
      
      choice = input("Selecciona una opción: ")
      if choice == "1":
        self.get_pg_cards()
      elif choice == "2":
        self.insert_card_manually()
      elif choice == "3":
        print("programa la weá luego jeropa")
      elif choice == "4":
        break
      else:
        print("Elige una opción valida")
      
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

    card_types = self.pg_db.get_card_types()
    while True:
      card_type = input("Enter card type: ")
      if card_type in card_types:
        break
      print("\ncard type should be a valid type: ")
      for ct in card_types:
        print(ct)
      print("\n")
      
    card = Card(card_name, card_description, card_type)
    self.pg_db.insert_card_manually(card)
    print("\nCard has been added to the db")
    
  def get_pg_cards(self):
    cards = self.pg_db.get_cards_data()
    if cards:
      for card in cards:
        print(f"\nID: {card[0]} \nName: {card[1]} \nDescription: {card[2]} \nType: {card[3]}")
    else: 
      print("no cards")
    
m1 = Menu()
m1.insert_card_manually()
