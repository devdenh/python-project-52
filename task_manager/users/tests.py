from django.core.exceptions import ObjectDoesNotExist
from task_manager.users.models import User
from django.test import TestCase
from task_manager.utils import get_fixture_data
from django.urls import reverse


class UserTest(TestCase):
    fixtures = ["statuses.json", "users.json"]

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.first()
        cls.test_data = get_fixture_data('test_data.json')

    def test_index_page(self):
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(reverse('users:create'),
                                    self.test_data['users']['new'])

        self.assertRedirects(response, reverse('login'))

        user = User.objects.get(
            username=self.test_data['users']['new']['username']
        )
        self.assertEqual(user.username,
                         self.test_data['users']['new']['username'])

    def test_update_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:update', args=[self.user.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:update', args=[self.user.pk]),
                                    self.test_data['users']['new'])

        self.assertRedirects(response, reverse('users:index'))
        updated_user = User.objects.get(
            username=self.test_data['users']['new']['username']
        )
        self.assertEqual(updated_user.username,
                         self.test_data['users']['new']['username'])

    def test_delete_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:delete', args=[self.user.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:delete', args=[self.user.pk]))

        self.assertRedirects(response, reverse('users:index'))

        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(
                username=self.test_data['users']['existing']['username']
            )
