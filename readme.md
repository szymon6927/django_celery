# Django Celery

Example project which was created as a part of Netguru goals
which shows a simple configuration Django + Celery


## Django 

Create a virtual environment

```
$ python3.7 -m venv venv
```

Run a virtualenv environment

```
$ source venv/bin/activate
```

Install required packages with dev dependencies

```
pip install -r requirements.txt
```

Run app locally 

```
$ python manage.py runserver
```



## Rabbit-MQ

To run Rabbit-MQ locally

```bash
$ docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:management
```

## Celery

To run Celery

```
celery -A django_celery worker -l info
```
