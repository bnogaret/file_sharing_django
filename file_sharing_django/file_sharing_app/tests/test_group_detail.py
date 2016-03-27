from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .. models import Group

class GroupDetailTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("dummy", "test.test@test.com", "test")
        self.group = Group(name="group test", creator=self.user)
        self.client = Client()

    def test_page_need_authenticated_user(self):
        response = self.client.get(reverse("file_sharing_app:group_detail", kwargs={'group_id': 1}))
        self.assertRedirects(response, '%s?next=/group/1' % reverse("file_sharing_app:login"))

    def test_page_existring_group_id(self):
        self.client.login(username=self.user.username, password="test")
        response = self.client.get(reverse("file_sharing_app:group_detail", kwargs={'group_id': 2}))
        self.assertEqual(response.status_code, 404)
