import os
import requests
import time

def reset_database():
    """Reset the database and add all recipes"""
    
    # Remove the database file if it exists
    db_path = "backend/recipes.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print("🗑️  Deleted existing database file")
    
    # Wait a moment for the file to be deleted
    time.sleep(2)
    
    # Test the API to see if it's working
    try:
        response = requests.get('http://localhost:5000/api/recipes')
        if response.status_code == 200:
            recipes = response.json()
            print(f"✅ Database reset successful! Found {len(recipes)} recipes")
            
            # Show all recipes
            print("\n🍳 ALL RECIPES IN DATABASE:")
            print("=" * 80)
            
            for i, recipe in enumerate(recipes, 1):
                print(f"{i}. {recipe['title']}")
                print(f"   Description: {recipe['description']}")
                print(f"   Calories: {recipe['calories']} | Cooking Time: {recipe['cooking_time']} min | Servings: {recipe['servings']}")
                print("-" * 80)
            
            # Test search functionality
            print("\n🔍 TESTING SEARCH FUNCTIONALITY:")
            search_terms = ['chicken', 'rice', 'bowl', 'pasta', 'beef', 'shrimp', 'mushroom', 'chocolate']
            
            for term in search_terms:
                filtered_recipes = [
                    recipe for recipe in recipes 
                    if term.lower() in recipe['title'].lower()
                ]
                
                print(f"\nSearch for '{term}':")
                if filtered_recipes:
                    for recipe in filtered_recipes:
                        print(f"  - {recipe['title']}")
                else:
                    print(f"  No recipes found matching '{term}'")
            
            return recipes
        else:
            print(f"❌ Error: API returned status code {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error connecting to API: {e}")
        return []

if __name__ == "__main__":
    print("🔄 Resetting database and testing recipes...")
    recipes = reset_database()
    
    if recipes:
        print(f"\n📊 TOTAL RECIPES: {len(recipes)}")
    else:
        print("❌ No recipes found or API not accessible") 