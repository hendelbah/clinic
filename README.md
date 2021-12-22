# EPAM final project - Clinic app

[![Coverage Status](https://coveralls.io/repos/github/hendelbah/clinic/badge.svg?branch=main)](https://coveralls.io/github/hendelbah/clinic?branch=main)
[![Build Status](https://app.travis-ci.com/hendelbah/clinic.svg?branch=main)](https://app.travis-ci.com/hendelbah/clinic)

#### Web app for managing appointments in a clinic

## With this app you can:

- #### Log in as an administrator or a doctor
- #### Display a list of users
- #### Display a list of doctors
- #### Display a list of patients
- #### Display a list of appointments and the total income from them
- #### Change (add / edit / delete) the above data

## How to build this project:

- #### Navigate to the project root folder

- #### Optionally set up and activate the virtual environment:

```
virtualenv venv
source venv/bin/activate
```

- #### Install the requirements:

```
pip install -r requirements.txt
```

- #### Configure MySQL database

- #### Set the following environment variables:

```
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_user_password>
MYSQL_SERVER=<your_mysql_server>
MYSQL_DATABASE=<your_mysql_database_name>
FLASK_APP=clinic_app
```

- ##### Optionally set:

```
FLASK_SECRET_KEY=<your_secure_key>
FLASK_CONFIG=production
```

- #### Run migrations to create database infrastructure:

```
flask db upgrade
```

- #### Optionally populate the database with sample data

```
python -m clinic_app/service/populate
```

- #### Run the project locally:

```
python -m flask run
```

## Now you should be able to access the web service and web application:

### Web Service (API):

```
localhost:5000/api/users?search_email=<str>
localhost:5000/api/users/<uuid>
localhost:5000/api/doctors?search_name=<str>&no_user=<1 or nothing>
localhost:5000/api/doctors/<uuid>
localhost:5000/api/patients?search_phone=<str>&search_name=<str>
localhost:5000/api/patients/<uuid>
localhost:5000/api/appointments?doctor_uuid=<str>&patient_uuid=<str>&doctor_name=<str>&patient_name=<str>&date_from=<YYYY-MM-DD>&date_to=<YYYY-MM-DD>
localhost:5000/api/appointments/<uuid>
localhost:5000/api/appointments/stats?<same filters as for appointments>
```

Also, all collection resources accept `page` and `per_page` GET parameters

### Web Application:

#### After population, to log in you can use following email - password:

- ##### `root` - `root1234`: admin user
- ##### `doctor_001@spam.ua` - `doctor1234`: admin and doctor user

#### Routes:
```
localhost:5000/
localhost:5000/doctors

localhost:5000/login
localhost:5000/logout
localhost:5000/profile

localhost:5000/admin-panel/

localhost:5000/admin-panel/users
localhost:5000/admin-panel/users/new
localhost:5000/admin-panel/users/<uuid>
localhost:5000/admin-panel/users/<uuid>/delete

localhost:5000/admin-panel/doctors
localhost:5000/admin-panel/doctors/new
localhost:5000/admin-panel/doctors/<uuid>
localhost:5000/admin-panel/doctors/<uuid>/delete

localhost:5000/admin-panel/patients
localhost:5000/admin-panel/patients/new
localhost:5000/admin-panel/patients/<uuid>
localhost:5000/admin-panel/patients/<uuid>/delete

localhost:5000/admin-panel/appointments
localhost:5000/admin-panel/appointments/new
localhost:5000/admin-panel/appointments/<uuid>
localhost:5000/admin-panel/appointments/<uuid>/delete
```