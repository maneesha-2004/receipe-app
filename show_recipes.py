import requests
import json

def show_all_recipes():
    """Display all recipes in the database"""
    try:
        response = requests.get('http://localhost:5000/api/recipes')
        if response.status_code == 200:
            recipes = response.json()
            print("🍳 ALL RECIPES IN DATABASE:")
            print("=" * 80)
            
            for i, recipe in enumerate(recipes, 1):
                print(f"{i}. {recipe['title']}")
                print(f"   Description: {recipe['description']}")
                print(f"   Calories: {recipe['calories']} | Cooking Time: {recipe['cooking_time']} min | Servings: {recipe['servings']}")
                print(f"   Video URL: {recipe['video_url']}")
                print("-" * 80)
            
            return recipes
        else:
            print(f"Error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error connecting to API: {e}")
        return []

def test_search(search_term):
    """Test search functionality"""
    try:
        response = requests.get('http://localhost:5000/api/recipes')
        if response.status_code == 200:
            recipes = response.json()
            
            # Filter recipes based on search term
            filtered_recipes = [
                recipe for recipe in recipes 
                if search_term.lower() in recipe['title'].lower()
            ]
            
            print(f"\n🔍 SEARCH RESULTS FOR '{search_term}':")
            print("=" * 60)
            
            if filtered_recipes:
                for i, recipe in enumerate(filtered_recipes, 1):
                    print(f"{i}. {recipe['title']}")
                    print(f"   Description: {recipe['description']}")
                    print(f"   Calories: {recipe['calories']} | Cooking Time: {recipe['cooking_time']} min")
                    print("-" * 60)
            else:
                print(f"No recipes found matching '{search_term}'")
            
            return filtered_recipes
        else:
            print(f"Error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    # Show all recipes
    recipes = show_all_recipes()
    
    if recipes:
        print(f"\n📊 TOTAL RECIPES: {len(recipes)}")
        
        # Test search functionality
        print("\n" + "="*80)
        test_search("chicken")
        print("\n" + "="*80)
        test_search("rice")
        print("\n" + "="*80)
        test_search("bowl")
        print("\n" + "="*80)
        test_search("pasta")
        print("\n" + "="*80)
        test_search("beef")
    else:
        print("No recipes found or API not accessible") 