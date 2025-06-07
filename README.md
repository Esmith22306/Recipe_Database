
# Overview

The program is written in Python and integrates with a SQLite relational database. Users interact with the software via a terminal-based menu. It demonstrates CRUD (Create, Read, Update, Delete) operations and joins between two tables (`Recipes` and `Ingredients`).

This project helped me deepen my understanding of SQL syntax, Python’s `sqlite3` module, and how to manage persistent data storage.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The software uses a **SQLite** relational database called `recipes.db`. It consists of two related tables:

- **Recipes**  
  - `id` (Primary Key)  
  - `name` (Text)  
  - `category` (Text)  
  - `date_added` (Date)

- **Ingredients**  
  - `id` (Primary Key)  
  - `recipe_id` (Foreign Key referencing `Recipes.id`)  
  - `name` (Text)  
  - `quantity` (Text)

The `Ingredients` table uses a foreign key relationship to link ingredients to their respective recipes.

# Development Environment

- **Python 3.x**
- **SQLite** via Python’s built-in `sqlite3` module


# Useful Websites

- [SQLite Official Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)


# Future Work

- Add support for editing ingredients in a recipe
- Implement search/filter functionality by category or keyword
- Create a GUI version using Tkinter or PyQt
- Add ability to export/import recipe data to/from files
