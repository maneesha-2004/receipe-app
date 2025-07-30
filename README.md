# Recipe Management Application

A full-stack recipe application built with Flask (backend), React (frontend), and SQLite (database).

## Features

- **Recipe Management**: Create, edit, and view recipes with ingredients, quantities, and nutritional info
- **Cooking Process**: Step-by-step cooking instructions
- **Video Recommendations**: Embedded cooking videos for recipes
- **Online Ordering**: Order ingredients online
- **User Authentication**: Secure user registration and login
- **Responsive Design**: Modern UI that works on all devices

## Tech Stack

### Backend
- Flask (Python web framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Flask-CORS (Cross-origin resource sharing)
- Flask-JWT-Extended (Authentication)

### Frontend
- React (JavaScript framework)
- Axios (HTTP client)
- React Router (Navigation)
- CSS3 (Styling)

## Project Structure

```
maniniki/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.js
│   └── package.json
└── README.md
```

## Setup Instructions

### Backend Setup
1. Navigate to backend directory: `cd backend`
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the Flask app: `python app.py`

### Frontend Setup
1. Navigate to frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the React app: `npm start`

## API Endpoints

- `GET /api/recipes` - Get all recipes
- `POST /api/recipes` - Create new recipe
- `GET /api/recipes/<id>` - Get specific recipe
- `PUT /api/recipes/<id>` - Update recipe
- `DELETE /api/recipes/<id>` - Delete recipe
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/orders` - Create order

## Database Schema

- **Users**: id, username, email, password_hash
- **Recipes**: id, title, description, servings, calories, cooking_time, video_url
- **Ingredients**: id, name, category
- **RecipeIngredients**: recipe_id, ingredient_id, quantity, unit
- **CookingSteps**: id, recipe_id, step_number, instruction
- **Orders**: id, user_id, recipe_id, quantity, order_date, status