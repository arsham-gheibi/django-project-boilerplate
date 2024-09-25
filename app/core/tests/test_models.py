"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


def create_user(
    email='test@example.com',
    password='testpass123'
):
    """ Create and return a new user """
    return get_user_model().objects.create_user(
        email=email,
        password=password
    )


class ModelTests(TestCase):
    """ Test Models """

    def test_create_user_with_email_successfull(self):
        """ Test creating a user with email is successful """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test Email is normalized for new users """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, excepted in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, excepted)

    def test_new_user_without_email_raises_error(self):
        """ Test Creating a user without an email raises ValidationError """
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user('', 'test123')

    def test_new_user_with_invalid_email_raises_error(self):
        """ Test Creating a user with an invalid email raises ValusError """
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user('not_an_email', 'test123')

    def test_create_superuser(self):
        """ Test Crating a superuser """
        user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'superpassword123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
