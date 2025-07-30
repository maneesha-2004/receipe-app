import sqlite3
import os

def test_database():
    """Test the database directly"""
    
    db_path = "backend/recipes.db"
    
    if not os.path.exists(db_path):
        print("❌ Database file does not exist!")
        return
    
    print(f"✅ Database file exists: {db_path}")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"📋 Tables in database: {[table[0] for table in tables]}")
    
    # Check recipes
    try:
        cursor.execute("SELECT * FROM recipe;")
        recipes = cursor.fetchall()
        print(f"🍳 Recipes in database: {len(recipes)}")
        
        for i, recipe in enumerate(recipes, 1):
            print(f"  {i}. {recipe[1]} - {recipe[2]}")  # title and description
    except Exception as e:
        print(f"❌ Error reading recipes: {e}")
    
    # Check ingredients
    try:
        cursor.execute("SELECT * FROM ingredient;")
        ingredients = cursor.fetchall()
        print(f"🥕 Ingredients in database: {len(ingredients)}")
    except Exception as e:
        print(f"❌ Error reading ingredients: {e}")
    
    conn.close()

if __name__ == "__main__":
    test_database() 