# MODELLING RELATIONSHIPS IN FLASK

## Procedures

1. Install a virtual environment
```bash
pipenv install
```
2. Shell inside it
```bash
pipenv shell
```
3. Install all dependancies 
```bash
pipenv install flask
```
```bash
pipenv install flask-sqlalchemy
```
```bash
pipenv install flask-migrate
```

## Run Migration
```bash
flask db init
```
```bash
flask db migrate -m "Intial migration"
```
```bash
flask db upgrade
```

## Seeding

To seed for one to one relationship run:
```bash
python seed_one_to_one.py
```
To seed for one to many relationship run:
```bash
python seed_one_to_many.py
```
To seed for many to many relationship run:
```bash
python seed_many_to_many.py
```
