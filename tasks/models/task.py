from django.db import models

from tasks.models import Tag


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return self.content[:30]
