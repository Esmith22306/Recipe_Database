import sqlite3


# Opens a connection to SQLite database named recipes.db 
# If the file doesent exist SQLite will create it. 
def connect_db():
    return sqlite3.connect("recipes.db")


# Create two tables if they dont already exist. 
def create_tables():
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        date_added DATE DEFAULT (date('now'))
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        name TEXT NOT NULL,
        quantity TEXT,
        FOREIGN KEY (recipe_id) REFERENCES Recipes(id)
    )
    """)

    conn.commit()
    conn.close()


# User Prompt for entering a recipe name and category. 
# Inserts that into the recipes table. 
# Then prompts the user to enter multiple ingredients ("Until they type done")
def add_recipe():
    name = input("Recipe name: ")
    category = input("Category (e.g. Dessert, Main, etc.): ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Recipes (name, category) VALUES (?, ?)", (name, category))
    recipe_id = cursor.lastrowid

    print("Enter ingredients (type 'done' to finish):")
    while True:
        ingredient = input("Ingredient name: ")
        if ingredient.lower() == 'done':
            break
        quantity = input("Quantity: ")
        cursor.execute("INSERT INTO Ingredients (recipe_id, name, quantity) VALUES (?, ?, ?)",
                       (recipe_id, ingredient, quantity))

    conn.commit()

    conn.close()
    print("Recipe added successfully!\n")

# Loops through results grouping by recipe ID.
def view_recipes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Recipes.id, Recipes.name, Recipes.category, Recipes.date_added,
               Ingredients.name, Ingredients.quantity
        FROM Recipes
        LEFT JOIN Ingredients ON Recipes.id = Ingredients.recipe_id
        ORDER BY Recipes.id
    """)
    rows = cursor.fetchall()
    conn.close()

    current_recipe = None
    for row in rows:
        recipe_id, name, category, date_added, ingredient, quantity = row
        if recipe_id != current_recipe:
            print(f"\nRecipe #{recipe_id}: {name} ({category}) - Added on {date_added}")
            current_recipe = recipe_id
        if ingredient:
            print(f"  - {ingredient} ({quantity})")


# Asks for a recipe ID, a new name and a new category. 
def update_recipe():
    recipe_id = input("Enter recipe ID to update: ")
    new_name = input("New recipe name: ")
    new_category = input("New category: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Recipes SET name = ?, category = ? WHERE id = ?", (new_name, new_category, recipe_id))
    conn.commit()
    conn.close()
    print("Recipe updated successfully.\n")


# Asks for recipe ID and deletes all related entries from the ingrediants table 
# Deletes the recipe from the recipes table
def delete_recipe():
    recipe_id = input("Enter recipe ID to delete: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Ingredients WHERE recipe_id = ?", (recipe_id,))
    cursor.execute("DELETE FROM Recipes WHERE id = ?", (recipe_id,))
    conn.commit()
    conn.close()
    print("Recipe deleted successfully.\n")


# Loop with 5 options displayed
# Each input calls a different function
def main():
    create_tables()
    while True:
        print("\n--- Recipe Manager ---")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Update Recipe")
        print("4. Delete Recipe")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            update_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
