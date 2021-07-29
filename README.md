# Scheduler

## Installation

````shell
git clone https://github.com/fcramos/scheduler
cd scheduler
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
touch .env
````
### Database config
Create scheduler database

#### MySQL database
```pip install mysqlclient```

Set url database

msql://user:password@localhost/scheduler

#### PostgreSQL
```pip install psycopg2-binary```

Set url database

postgres://postgres:fcr-9194@localhost/scheduler

### Secret key
```python -c "import secrets; print(secrets.token_urlsafe())"```

### Config file
````shell
vim .env
````
````.ini
SECRET_KEY=<past here secret_key>
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=<paste here url database>
````

### Start project
````shell
python manage.py migrate
python manage.py test
python manage.py runserver
````

## Getting start

### Create a scheduling
````
curl -d '{"method": 1, "timestamp": "2021-07-29T12:00:00", "receiver": "Jon Do", "message": "Good morning"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/scheduling
````

### Get all schedulings
````
curl -H "Content-Type: application/json" -X GET http://localhost:8000/api/scheduling
````

### Get a specific scheduling
````
curl -H "Content-Type: application/json" -X GET http://localhost:8000/api/scheduling/<id>
````

### Change a scheduling
````
curl -d '{"method": 1, "timestamp": "2021-07-29T12:00:00", "receiver": "Jon Do", "message": "Good morning", "status": 1}' -H "Content-Type: application/json" -X PUT http://localhost:8000/api/scheduling/<id>
````

### Delete a scheduling
````
curl -H "Content-Type: application/json" -X DELETE http://localhost:8000/api/scheduling/<id>
````
