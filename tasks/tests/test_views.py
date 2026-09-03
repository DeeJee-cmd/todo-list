from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task


class TaskViewTests(TestCase):

    def setUp(self):
        self.task = Task.objects.create(content="Test Task", is_done=False)
        self.tag = Tag.objects.create(name="Test Tag")

    def test_task_list_view(self):
        response = self.client.get(reverse("tasks:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_list.html")
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        response = self.client.post(
            reverse("tasks:task-create"),
            {"content": "New Task", "tags": [self.tag.pk]},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_task_toggle_status_view(self):
        response = self.client.post(
            reverse("tasks:task-toggle", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

    def test_tag_list_view(self):
        response = self.client.get(reverse("tasks:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/tag_list.html")
        self.assertContains(response, "Test Tag")

    def test_tag_delete_view(self):
        response = self.client.post(
            reverse("tasks:tag-delete", kwargs={"pk": self.tag.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())
