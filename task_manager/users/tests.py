from task_manager.users.models import User
from django.test import TestCase
from task_manager.utils import get_fixture_data
from django.urls import reverse


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_fixture_data('test_data.json')

    def test_index_page(self):
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        # new_data = self.test_data[0]['fields']
        response = self.client.post(reverse('users:create'), {'username': 'somename'})
        print(User.objects.all())
        print(response.context)
