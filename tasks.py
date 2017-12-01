from celery import Celery

app = Celery('tasks', broker='pyamp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
