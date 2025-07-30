import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('backend')

# Import the models
from backend.models import db, Recipe, Ingredient, RecipeIngredient, CookingStep
from backend.config import Config

def create_test_app():
    """Create a test Flask app to initialize the database"""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

def reset_and_populate_database():
    """Reset the database and populate with all recipes"""
    
    # Remove existing database
    db_path = "backend/recipes.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print("🗑️  Deleted existing database file")
    
    # Create Flask app and initialize database
    app = create_test_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Created database tables")
        
        # Add ingredients
        ingredients = [
            Ingredient(name='Chicken Breast', category='Protein', price_per_unit=8.99, unit='kg'),
            Ingredient(name='Rice', category='Grains', price_per_unit=2.99, unit='kg'),
            Ingredient(name='Tomato', category='Vegetables', price_per_unit=3.99, unit='kg'),
            Ingredient(name='Onion', category='Vegetables', price_per_unit=1.99, unit='kg'),
            Ingredient(name='Garlic', category='Vegetables', price_per_unit=4.99, unit='kg'),
            Ingredient(name='Olive Oil', category='Oils', price_per_unit=12.99, unit='L'),
            Ingredient(name='Salt', category='Seasonings', price_per_unit=1.99, unit='kg'),
            Ingredient(name='Black Pepper', category='Seasonings', price_per_unit=5.99, unit='kg'),
            Ingredient(name='Pasta', category='Grains', price_per_unit=3.99, unit='kg'),
            Ingredient(name='Ground Beef', category='Protein', price_per_unit=12.99, unit='kg'),
            Ingredient(name='Cheese', category='Dairy', price_per_unit=8.99, unit='kg'),
            Ingredient(name='Milk', category='Dairy', price_per_unit=2.99, unit='L'),
            Ingredient(name='Butter', category='Dairy', price_per_unit=6.99, unit='kg'),
            Ingredient(name='Flour', category='Grains', price_per_unit=2.49, unit='kg'),
            Ingredient(name='Eggs', category='Protein', price_per_unit=4.99, unit='dozen'),
            Ingredient(name='Bell Pepper', category='Vegetables', price_per_unit=3.99, unit='kg'),
            Ingredient(name='Mushrooms', category='Vegetables', price_per_unit=5.99, unit='kg'),
            Ingredient(name='Spinach', category='Vegetables', price_per_unit=4.99, unit='kg'),
            Ingredient(name='Lemon', category='Fruits', price_per_unit=2.99, unit='kg'),
            Ingredient(name='Basil', category='Herbs', price_per_unit=3.99, unit='bunch'),
            Ingredient(name='Shrimp', category='Protein', price_per_unit=15.99, unit='kg'),
            Ingredient(name='Chocolate', category='Baking', price_per_unit=8.99, unit='kg'),
            Ingredient(name='Sugar', category='Baking', price_per_unit=2.49, unit='kg'),
            Ingredient(name='Vanilla Extract', category='Baking', price_per_unit=12.99, unit='L')
        ]
        
        for ingredient in ingredients:
            db.session.add(ingredient)
        db.session.commit()
        print(f"✅ Added {len(ingredients)} ingredients")
        
        # Add all recipes with YouTube videos and images
        recipes = [
            Recipe(
                title='Chicken Rice Bowl',
                description='Delicious chicken rice bowl with tender chicken, fluffy rice, and fresh vegetables',
                servings=4,
                calories=420,
                cooking_time=30,
                video_url='https://www.youtube.com/embed/dQw4w9WgXcQ',
                image_url='https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400'
            ),
            Recipe(
                title='Chicken 65',
                description='Flavorful spicy chicken 65 with fresh chicken and crunchy texture',
                servings=4,
                calories=380,
                cooking_time=25,
                video_url='https://youtu.be/Hs4JIgNJ6m8?si=X5yi3QCSLaYOkxAk',
                image_url='https://theflavoursofkitchen.com/wp-content/uploads/2021/08/Chicken-65-3-scaled.jpg'
            ),
            Recipe(
                title='Classic Spaghetti Carbonara',
                description='Authentic Italian pasta dish with eggs, cheese, and pancetta',
                servings=2,
                calories=650,
                cooking_time=20,
                video_url='https://www.youtube.com/embed/jB0vCvJqsh8',
                image_url='https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=400'
            ),
            Recipe(
                title='Beef Tacos',
                description='Flavorful Mexican tacos with seasoned ground beef and fresh toppings',
                servings=6,
                calories=350,
                cooking_time=25,
                video_url='https://www.youtube.com/embed/8T8jvltC_ug',
                image_url='https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=400'
            ),
            Recipe(
                title='Chocolate Chip Cookies',
                description='Classic homemade chocolate chip cookies with crispy edges and chewy centers',
                servings=24,
                calories=150,
                cooking_time=45,
                video_url='https://www.youtube.com/embed/AEPjP916A7Q',
                image_url='https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=400'
            ),
            Recipe(
                title='Shrimp Fried Rice',
                description='Delicious shrimp fried rice with vegetables and soy sauce',
                servings=4,
                calories=350,
                cooking_time=25,
                video_url='https://www.youtube.com/embed/dQw4w9WgXcQ',
                image_url='https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400'
            ),
            Recipe(
                title='Mushroom Risotto',
                description='Creamy Italian risotto with wild mushrooms and parmesan cheese',
                servings=4,
                calories=420,
                cooking_time=35,
                video_url='https://www.youtube.com/embed/jB0vCvJqsh8',
                image_url='https://images.unsplash.com/photo-1621996346565-e3dbc353d2e5?w=400'
            ),
            Recipe(
                title='Chocolate Lava Cake',
                description='Decadent chocolate lava cake with molten center and vanilla ice cream',
                servings=4,
                calories=280,
                cooking_time=20,
                video_url='https://www.youtube.com/embed/AEPjP916A7Q',
                image_url='https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=400'
            )
        ]
        
        for recipe in recipes:
            db.session.add(recipe)
        db.session.commit()
        print(f"✅ Added {len(recipes)} recipes")
        
        # Add cooking steps for each recipe
        cooking_steps = [
            # Chicken Rice Bowl
            CookingStep(recipe_id=1, step_number=1, description='Cook rice according to package instructions'),
            CookingStep(recipe_id=1, step_number=2, description='Season chicken with salt and pepper'),
            CookingStep(recipe_id=1, step_number=3, description='Cook chicken in olive oil until golden brown'),
            CookingStep(recipe_id=1, step_number=4, description='Chop vegetables and prepare toppings'),
            CookingStep(recipe_id=1, step_number=5, description='Assemble bowl with rice, chicken, and vegetables'),
            
            # Chicken 65
            CookingStep(recipe_id=2, step_number=1, description='Marinate chicken with spices and yogurt'),
            CookingStep(recipe_id=2, step_number=2, description='Heat oil in a deep pan'),
            CookingStep(recipe_id=2, step_number=3, description='Fry chicken pieces until crispy'),
            CookingStep(recipe_id=2, step_number=4, description='Add curry leaves and final spices'),
            CookingStep(recipe_id=2, step_number=5, description='Serve hot with mint chutney'),
            
            # Spaghetti Carbonara
            CookingStep(recipe_id=3, step_number=1, description='Boil pasta in salted water'),
            CookingStep(recipe_id=3, step_number=2, description='Cook pancetta until crispy'),
            CookingStep(recipe_id=3, step_number=3, description='Whisk eggs and cheese in a bowl'),
            CookingStep(recipe_id=3, step_number=4, description='Combine pasta with egg mixture'),
            CookingStep(recipe_id=3, step_number=5, description='Add black pepper and serve immediately'),
            
            # Beef Tacos
            CookingStep(recipe_id=4, step_number=1, description='Season ground beef with taco spices'),
            CookingStep(recipe_id=4, step_number=2, description='Cook beef in a skillet until browned'),
            CookingStep(recipe_id=4, step_number=3, description='Warm tortillas in a dry pan'),
            CookingStep(recipe_id=4, step_number=4, description='Chop fresh vegetables for toppings'),
            CookingStep(recipe_id=4, step_number=5, description='Assemble tacos with beef and toppings'),
            
            # Chocolate Chip Cookies
            CookingStep(recipe_id=5, step_number=1, description='Cream butter and sugar until fluffy'),
            CookingStep(recipe_id=5, step_number=2, description='Add eggs and vanilla extract'),
            CookingStep(recipe_id=5, step_number=3, description='Mix in flour, salt, and chocolate chips'),
            CookingStep(recipe_id=5, step_number=4, description='Drop spoonfuls onto baking sheet'),
            CookingStep(recipe_id=5, step_number=5, description='Bake at 350°F for 10-12 minutes'),
            
            # Shrimp Fried Rice
            CookingStep(recipe_id=6, step_number=1, description='Cook rice and let it cool'),
            CookingStep(recipe_id=6, step_number=2, description='Stir-fry shrimp until pink'),
            CookingStep(recipe_id=6, step_number=3, description='Add vegetables and stir-fry'),
            CookingStep(recipe_id=6, step_number=4, description='Add rice and soy sauce'),
            CookingStep(recipe_id=6, step_number=5, description='Garnish with green onions and serve'),
            
            # Mushroom Risotto
            CookingStep(recipe_id=7, step_number=1, description='Sauté mushrooms in olive oil'),
            CookingStep(recipe_id=7, step_number=2, description='Add rice and toast for 2 minutes'),
            CookingStep(recipe_id=7, step_number=3, description='Add hot broth gradually while stirring'),
            CookingStep(recipe_id=7, step_number=4, description='Cook until rice is creamy'),
            CookingStep(recipe_id=7, step_number=5, description='Stir in parmesan cheese and serve'),
            
            # Chocolate Lava Cake
            CookingStep(recipe_id=8, step_number=1, description='Melt chocolate and butter together'),
            CookingStep(recipe_id=8, step_number=2, description='Whisk eggs and sugar until pale'),
            CookingStep(recipe_id=8, step_number=3, description='Fold chocolate mixture into eggs'),
            CookingStep(recipe_id=8, step_number=4, description='Pour into greased ramekins'),
            CookingStep(recipe_id=8, step_number=5, description='Bake at 425°F for 12-14 minutes')
        ]
        
        for step in cooking_steps:
            db.session.add(step)
        db.session.commit()
        print(f"✅ Added {len(cooking_steps)} cooking steps")
        
        # Verify the database
        recipe_count = Recipe.query.count()
        ingredient_count = Ingredient.query.count()
        step_count = CookingStep.query.count()
        
        print(f"\n📊 DATABASE SUMMARY:")
        print(f"   Recipes: {recipe_count}")
        print(f"   Ingredients: {ingredient_count}")
        print(f"   Cooking Steps: {step_count}")
        
        return True

if __name__ == "__main__":
    print("🔄 Resetting and populating database...")
    success = reset_and_populate_database()
    
    if success:
        print("\n✅ Database successfully reset and populated!")
        print("🌐 You can now access the application at http://localhost:3000")
        print("🔍 Search for recipes like 'chicken', 'rice', 'pasta', 'beef', 'shrimp', 'mushroom', 'chocolate'")
    else:
        print("❌ Failed to reset database") 