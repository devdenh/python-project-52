from django.core.exceptions import ObjectDoesNotExist
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.test import TestCase
from task_manager.utils import get_fixture_data
from django.urls import reverse


class StatusesTest(TestCase):
    fixtures = ["statuses.json", "users.json", "labels.json", "tasks.json"]
    test_data = get_fixture_data('test_data.json')

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.first()
        cls.label = Label.objects.first()
        cls.label2 = Label.objects.get(pk=2)

    def test_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:index'))
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('labels:create'),
                                    self.test_data['labels']['new'])

        self.assertRedirects(response, reverse('labels:index'))

        label = Label.objects.get(name=self.test_data['labels']['new']['name'])
        self.assertEqual(label.name, self.test_data['labels']['new']['name'])

    def test_update_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:update', args=[self.label.pk]))

        self.assertEqual(response.status_code, 200)

    def test_update(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('labels:update', args=[self.label.pk]),
                                    self.test_data['labels']['new'])

        self.assertRedirects(response, reverse('labels:index'))

        updated_label = Label.objects.get(
            name=self.test_data['labels']['new']['name']
        )
        self.assertEqual(updated_label.name, self.test_data['labels']['new']['name'])

    def test_delete_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:delete', args=[self.label.pk]))

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('labels:delete', args=[self.label2.pk]))

        self.assertRedirects(response, reverse('labels:index'))

        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(
                name=self.label2.name
            )

    def test_bound_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(
            'labels:delete', args=[self.label.pk]), follow=True)

        assert Label.objects.get(pk=self.label.pk)
        message = "You can't delete labels are still being used"
        assert response.context['messages']._loaded_data[0].message == message
