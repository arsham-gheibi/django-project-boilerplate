"""
Database Models
"""
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """ Manager for users """

    def create_user(self, email, password=None, **extra_fields):
        """ Create, save and return a new user """
        validate_email(email)

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Create and return a new superuser """
        return self.create_user(
            email,
            password,
            is_superuser=True,
            is_staff=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    """ User in system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
