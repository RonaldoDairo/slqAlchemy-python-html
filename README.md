## on the folder from my terminal cmd  ||pip install virtualenv || soon python -m virtualenv venv || move to the folder Scripts them colocate in my  terminal activate . soon || code .

## f1 to looking for select interpreter and select python the start 
## f1 to looking for create new terminal 
## f1 to looking for formate and to download use black
## Flask SQLAlchemy CRUD || instalation pip install Flask-SQLAlchemy
## pip install mysqlclient
## to enter to the database mysql -h localhost -u root -p
this project is a CRUD application using flask and mysql using SQLAlchemy

### Installation with docker-compose

```

cd flask-sqlalchemy-crud
docker-compose up
```

### Manual Installation

##### Requirements

* Python3
* Mysql

before run the app you must create the following environnment variables:

```
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DATABASE=
MYSQL_HOST=
MYSQL_PORT=
```

```

cd flask-sqlalchemy-crud
pip install -r requirements.txt
python index.py
```
