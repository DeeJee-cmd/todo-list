from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)