from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from .. forms import UserSignupForm

# Create your tests here.

class UserSignupFormTests(TestCase):
    def setUp(self):
        User.objects.create_user("dummy", "test.test@test.com", "test")

    def test_create_user_without_email(self):
        """
        Email is required field, it shouldn't add a new User without it.
        """
        form_data = {
            'username': "azertyuiop",
            'password1': "tt",
            'password2': "tt",
        }
        form = UserSignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username=form_data['username'])

    def test_create_user_already_existing(self):
        """
        Check that we can't the form is not calid if we try to create a new User
        with a username already existing.
        """
        form_data = {
            'username': "dummy",
            'email': "truc@gotmail.com",
            'password1': "tt",
            'password2': "tt",
        }
        form = UserSignupForm(data=form_data)
        self.assertFalse(form.is_valid())

class UserSignupPageTest(TestCase):
    def setUp(self):
        User.objects.create_user("dummy", "test.test@test.com", "test")
        self.client = Client()

    def test_signup_page_redirect_to_index(self):
        """
        Check that correct information create a user, and redirect to the
        index page.
        """
        form_data = {
            'username': "test",
            'email': "truc@gotmail.com",
            'password1': "test1345",
            'password2': "test1345",
        }
        response = self.client.post(reverse("file_sharing_app:sign_up"), form_data)
        self.assertRedirects(response, reverse("file_sharing_app:index"))

    def test_signup_page_create_user(self):
        """
        Check that correct information create a new user in the database
        """
        form_data = {
            'username': "gd_yzeiuk",
            'email': "truc@gotmail.com",
            'password1': "test1345",
            'password2': "test1345",
        }
        self.client.post(reverse("file_sharing_app:sign_up"), form_data)
        user = User.objects.get(username=form_data['username'])
        self.assertEqual(user.email, form_data['email'])
