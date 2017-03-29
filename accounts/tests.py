from django.test import TestCase
from django import forms
from django.conf import settings
from .models import User
from .forms import UserRegistrationForm

# TODO: This test DOES NOT work properly, meaning accounts don't work properly.
# You still need a username to avoid ValueError


class CustomUserTest(TestCase):

    def test_manager_create(self):
        user = User.objects._create_user("test@test.com", "password", False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password")

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1'
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Please enter your email address",
                                 form.full_clean())

    def test_registration_form_fails_with_passwords_not_matching(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3'
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_first_password_missing(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': '',
            'password2': 'letmein1'
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_fails_with_second_password_missing(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': ''
        })
        self.assertFalse(form.is_valid())