# Person

This one is a simple person application to manage the information for a person using REAST API.

### Steps to run the service locally:
#### Create and Activate virtual environment:
- Create virtual environment and activate it.


#### Install dependencies:
```
pip install -r requirements.txt
```
This will install all the dependencies on the virtual environment.

#### Set environment variables
Open `dev.env` file and add/update the values as required.

#### Create the tables:
Make sure you have MYSQL database locally with `account_db` database in it.
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
Make sure it runs without any error and verify that the tables are created in the database.

#### Start the service:

Start the application using below command:
```
python run.py
```
