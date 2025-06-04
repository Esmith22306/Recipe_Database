import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("recipe.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ingredients TEXT,
    instructions TEXT
)
""")

# Insert sample recipe
cursor.execute("""
INSERT INTO recipes (name, ingredients, instructions)
VALUES (?, ?, ?)
""", (
    "Grilled Cheese Sandwich",
    "Bread, Cheese, Butter",
    "Butter bread, add cheese, grill until golden."
))

# Commit insert
conn.commit()

# Query data
cursor.execute("SELECT * FROM recipes")
recipes = cursor.fetchall()

# Print results
for recipe in recipes:
    print(f"ID: {recipe[0]}, Name: {recipe[1]}, Ingredients: {recipe[2]}")

# Close connection
conn.close()
