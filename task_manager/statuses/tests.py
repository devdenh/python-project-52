from django.core.exceptions import ObjectDoesNotExist
from task_manager.statuses.models import Statuses
from task_manager.users.models import User
from django.test import TestCase
from task_manager.utils import get_fixture_data
from django.urls import reverse


class StatusesTest(TestCase):
    fixtures = ["statuses.json", "users.json", "tasks.json", "labels.json"]
    test_data = get_fixture_data('test_data.json')

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.first()
        cls.status = Statuses.objects.first()
        cls.status2 = Statuses.objects.get(pk=2)

    def test_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('statuses:create'),
                                    self.test_data['statuses']['new'])

        self.assertRedirects(response, reverse('statuses:index'))

        status = Statuses.objects.get(name=self.test_data['statuses']['new']['name'])
        self.assertEqual(status.name, self.test_data['statuses']['new']['name'])

    def test_update_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:update', args=[self.status.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('statuses:update', args=[self.status.pk]),
                                    self.test_data['statuses']['new'])

        self.assertRedirects(response, reverse('statuses:index'))

        updated_status = Statuses.objects.get(
            name=self.test_data['statuses']['new']['name']
        )
        self.assertEqual(updated_status.name, self.test_data['statuses']['new']['name'])

    def test_delete_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:delete', args=[self.status.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('statuses:delete', args=[self.status.pk]))

        self.assertRedirects(response, reverse('statuses:index'))

        with self.assertRaises(ObjectDoesNotExist):
            Statuses.objects.get(
                name=self.status.name
            )

    def test_bound_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(
            'statuses:delete', args=[self.status2.pk]), follow=True)

        assert Statuses.objects.get(pk=self.status2.pk)
        assert response.context['messages']._loaded_data[0].message

    def text_as_hexlet(self):
        self.client.force_login(self.user)
