import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("todos")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"
app.conf.result_backend = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"
app.conf.update(result_expires=60)

app.autodiscover_tasks()

app.conf.task_routes = (
    [
        ("todos.tasks.*", {"queue": "primary"}),
    ],
)

app.conf.beat_schedule = {
    "add": {
        "task": "todos.tasks.add",
        "schedule": 30,
    },
}