from django.core.exceptions import ObjectDoesNotExist
from task_manager.users.models import User
from django.test import TestCase
from task_manager.utils import get_fixture_data
from django.urls import reverse


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_fixture_data('users.json')

    def test_index_page(self):
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(reverse('users:create'),
                                    self.test_data[0]['fields'])

        self.assertRedirects(response, reverse('login'))

        user = User.objects.get(
            username=self.test_data[0]['fields']['username']
        )
        self.assertEqual(user.username,
                         self.test_data[0]['fields']['username'])

    def test_update_page(self):
        user = User.objects.create_user(self.test_data[0]['fields'])
        self.client.force_login(user)
        response = self.client.get(reverse('users:update', args=[user.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        new_user = User.objects.create_user(self.test_data[0]['fields'])
        self.client.force_login(new_user)
        response = self.client.post(reverse('users:update', args=[new_user.pk]),
                                    self.test_data[1]['fields'])

        self.assertRedirects(response, reverse('users:index'))
        updated_user = User.objects.get(
            username=self.test_data[1]['fields']['username']
        )
        self.assertEqual(updated_user.username, self.test_data[1]['fields']['username'])

    def test_delete_page(self):
        user = User.objects.create_user(self.test_data[0]['fields'])
        self.client.force_login(user)
        response = self.client.get(reverse('users:delete', args=[user.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        new_user = User.objects.create_user(self.test_data[0]['fields'])
        self.client.force_login(new_user)
        response = self.client.post(reverse('users:delete', args=[new_user.pk]))

        self.assertRedirects(response, reverse('users:index'))

        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(
                username=self.test_data[0]['fields']['username']
            )
