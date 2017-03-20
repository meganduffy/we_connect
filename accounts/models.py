"""
Settings.py -> AUTH_USER_MODEL = 'accounts.User'
"""
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


class AccountUserManager(UserManager):

    def create_user(self, username, email,
                    password, is_staff, is_superuser, **extra_fields):
        """
        Creates and save a User with the given username, email and password
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    objects = AccountUserManager()
    previous_login = models.DateTimeField(default=timezone.now)

    def is_subscribed(self, magazine):
        try:
            purchase = self.purchases.get(magazine__pk=magazine.pk)
        except Exception:
            return False

        if purchase.subscription_end < timezone.now():
            return False
        return True


