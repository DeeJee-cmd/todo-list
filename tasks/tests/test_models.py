from django.test import TestCase

from tasks.models import Tag, Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Python")
        self.task = Task.objects.create(content="Write tests")
        self.task.tags.add(self.tag)

    def test_task_str(self):
        self.assertEqual(str(self.task), "Write tests")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Python")

    def test_task_tag_relationship(self):
        self.assertIn(self.tag, self.task.tags.all())
