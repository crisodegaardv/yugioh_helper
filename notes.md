Main Menu:
  1. Check cards
  2. Check decks
  3. Check combos
  4. Exit



TODO:
1. Refactor of the db module.
 Reason: requiring the db_name to be passed every time isn't efficient. A better design would be to centralize the management of the database connection and make the class more streamlined for reuse.

Here’s how you can refactor your DatabaseManager to avoid repeatedly specifying the database name ✅


2. Create one option to get info from the db ✅

3. integrar env en el proyecto