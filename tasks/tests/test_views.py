from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task

User = get_user_model()

class TaskViewTests(TestCase):
    class TaskViewsTests(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username="testuser", password="password123")
            self.client.force_login(self.user)
            self.tag = Tag.objects.create(name="Work")
            self.task = Task.objects.create(content="Test task")
            self.task.tags.add(self.tag)

        def test_task_list_view(self):
            response = self.client.get(reverse("tasks:task-list"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Test task")

        def test_task_create_view(self):
            response = self.client.post(
                reverse("tasks:task-create"),
                {"content": "New Task", "tags": [self.tag.id]},
            )
            self.assertEqual(response.status_code, 302)
            self.assertTrue(Task.objects.filter(content="New Task").exists())

        def test_task_toggle_status_view(self):
            self.assertFalse(self.task.is_done)
            response = self.client.post(reverse("tasks:task-toggle", args=[self.task.id]))
            self.assertEqual(response.status_code, 302)
            self.task.refresh_from_db()
            self.assertTrue(self.task.is_done)

        def test_tag_list_view(self):
            response = self.client.get(reverse("tasks:tag-list"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Work")
