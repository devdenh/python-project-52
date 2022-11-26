from django.core.exceptions import ObjectDoesNotExist
from task_manager.statuses.models import Statuses
from task_manager.users.models import User
from task_manager.tasks.models import Task
from django.test import TestCase
from task_manager.utils import get_fixture_data
from django.urls import reverse


class StatusesTest(TestCase):
    fixtures = ["statuses.json", "users.json", "tasks.json", "labels.json"]
    test_data = get_fixture_data('test_data.json')

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.first()
        cls.task = Task.objects.first()
        cls.task2 = Task.objects.get(pk=2)

    def test_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tasks:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('tasks:create'),
                                    self.test_data['tasks']['new'])

        self.assertRedirects(response, reverse('tasks:index'))

        task = Task.objects.get(name=self.test_data['tasks']['new']['name'])
        self.assertEqual(task.name, self.test_data['tasks']['new']['name'])

    def test_update_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tasks:update', args=[self.task.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('tasks:update', args=[self.task.pk]),
                                    self.test_data['tasks']['new'])

        self.assertRedirects(response, reverse('tasks:index'))

        updated_task = Task.objects.get(
            name=self.test_data['tasks']['new']['name']
        )
        self.assertEqual(updated_task.name, self.test_data['tasks']['new']['name'])

    def test_delete_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tasks:delete', args=[self.task.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('tasks:delete', args=[self.task.pk]))

        self.assertRedirects(response, reverse('tasks:index'))

        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(
                name=self.task.name
            )

    def test_non_creator_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(
            'tasks:delete', args=[self.task2.pk]), follow=True)

        assert Statuses.objects.get(pk=self.task2.pk)
        message = "Only author can delete this task"
        assert response.context['messages']._loaded_data[0].message == message

    def test_filter_page(self):
        self.client.force_login(self.user)
        response = self.client.get("/tasks/?executor=2", follow=True)

        self.assertEqual(response.context["object_list"][0], self.task2)

    def test_author_only(self):
        self.client.force_login(self.user)
        response = self.client.get("/tasks/?author_only=on",
                                   follow=True)

        self.assertEqual(response.context["object_list"][0], self.task)
