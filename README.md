# Hotel Search App in Django

This project is a **Django-based Hotel Search Application** where users can search and sort hotels by price. It is built using **Django** for the backend, **Vue.js** for interactive UI, and **Bootstrap** for styling.

## Features

- **Sort Hotels**: Users can sort hotels by price (ascending or descending).
- **Price Filter**: Filter hotels within a price range using a slider.
- **Interactive Frontend**: Built using Vue.js for dynamic data updates without page reloads.
- **Stylish UI**: Bootstrap provides a modern and responsive interface.
- **Backend**: Django provides robust data handling with models, views, and APIs.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DhananjayTalekar/hotel_search.git
   
2. **Navigate to the Project Directory**:
   ```bash
   cd hotel_search
   
3. **Set Up a Virtual Environment**:
   ```bash
   venv env
   source env/bin/activate  # For Linux/Mac
   .\env\Scripts\activate.ps1   # For Windows
   
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   
5. **Migrate the Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   
7. **Run the development server**:
   ```bash
   python manage.py runserver
   
## Usage

1. Access the app in your browser at http://127.0.0.1:8000.
   
2.Navigate to the admin panel at http://127.0.0.1:8000/admin to add hotel details.

## Project Structure 

```bash
hotel_project/
│
├── home/
│   ├── migrations/
│   ├── templates/
│   │   └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── hotel_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
