# django_orange
This repository contains a simple Django project created for educational purposes.

### Description

Currently, the project only includes a single Django application named "catalog".

The mentioned features have not been implemented, but they are expected to be developed soon.

### Features

- Creating a specified amount of mock users with custom management CLI command
- Deleting users from the database with custom management CLI command
- Calculating hypotenuse with given catheti from user input (go to http://localhost:8000/triangle)
- Adding person to the database (go to http://localhost:8000/person)
- Updating person (go to go to http://localhost:8000/person/<id:int>)
- Logging request data and representing logs in admin panel for triangle app

### Usage

1. Clone this project repository to your destination folder
2. Create a virtual environment inside your project folder with command: python3 -m venv .venv
3. Activate your new virtual environment with command: source .venv/bin/activate
4. Install dependencies with command: pip install -r requirements.txt
5. Add your secret key to your virtual environment with command: export SECRET_KEY='your secret key' 
6. Run the application with command: python3 manage.py runserver
7. Go to http://localhost:8000 to see results

#### Used Python 3.10.6