# django_orange
This repository contains a simple Django project created for educational purposes.

### Description

The project only includes a single Django applications: "watches", "catalog", "triangle", "users"

### Various features

- Sending notification emails at specified time (go to http://localhost:8000/notification)(You will need to run RabbitMQ to do this)
- Creating a specified amount of mock users with custom management CLI command
- Deleting users from the database with custom management CLI command
- Calculating hypotenuse with given catheti from user input (go to http://localhost:8000/triangle)
- Adding person to the database (go to http://localhost:8000/person)
- Updating person (go to http://localhost:8000/person/<id:int>)
- Logging request data and representing logs in admin panel for triangle app

# Watches

### Setting up the project
- First you need to create virtual environment and install all dependencies:
```bash
python -m venv .venv  # creates new virtual environment
```

```bash
pip install -r requirements.txt  # installs all dependencies
```

```bash
source .venv/bin/activate  # activates your virtual environment
```

- Add SECRET_KEY to your environment variables:
```bash
export SECRET_KEY='$$$ My Secret Key $$$'  # add your secret key
```

- Migrate to set your database to actual project data structure:
```bash
./manage.py makemigrations
```
```bash
./manage.py migrate
```

- You can generate mock data for application with custom management command:
```bash
./manage.py create_mock_data 
 ```
- Deletion all mock data with command:
```bash
./manage.py delete_all_mock_data
```
- Create superuser to get access to django admin panel
```bash
./manage.py createsuperuser
```
- You can also use fixtures from fixtures.json file to load data to your database including superuser with commands:

```bash
python manage.py loaddata fixtures.json
```
- Run project:
```bash
./manage.py runserver 
```
- Go to http://127.0.0.1:8000/watches/ to use the app



#### Usage

1. Clone this project repository to your destination folder
2. Create a virtual environment inside your project folder with command: python3 -m venv .venv
3. Activate your new virtual environment with command: source .venv/bin/activate
4. Install dependencies with command: pip install -r requirements.txt
5. Add your secret key to your virtual environment with command: export SECRET_KEY='your secret key' 
6. Run the application with command: python3 manage.py runserver
7. Go to http://localhost:8000 to see results

#### Used Python 3.10.6