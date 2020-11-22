from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@will.com',
            password='testpass'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@will.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username='will',
            email='will@will.com',
            password='testpass'
        )
        self.assertEqual(superuser.username, 'will')
        self.assertEqual(superuser.email, 'will@will.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)