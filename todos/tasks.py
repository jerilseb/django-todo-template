from core.celery import app

@app.task
def add(x, y):
    print(f"Adding {x} and {y}")
    return x + y
