import sys
from termcolor import colored, cprint

class Menu:
  def __init__(self, db_name):
    self.db = db_name
  
  def main_menu(self):
    while True:
      cprint("\nMain Menu:", "yellow")
      cprint("1. Check cards", "cyan")
      cprint("2. Check decks", "cyan")
      cprint("3. Check combos", "cyan")
      cprint("4. Exit", "red")
      
      choice = input("Enter your choice: ")
      
      if choice == "1":
        print("hace esto")
      elif choice == "2":
        self.sub_menu_1()
      elif choice == "3":
        print("y este otro deah que le pasaba")
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
      
  def get_cards()