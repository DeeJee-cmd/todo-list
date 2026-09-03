from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.login_url = reverse("login")
        self.task_list_url = reverse("tasks:task-list")

    def test_anonymous_user_redirected_to_login(self):
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f"{self.login_url}?next={self.task_list_url}"
        )

    def test_authenticated_user_can_access_task_list(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.task_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_list.html")
