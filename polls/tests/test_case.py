from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    # ==========================================
    # Test Case 1 ~ Database Involved
    # ==========================================
    def test_create_user(self):
        user = User.objects.create(username = 'testuser')
        self.assertEqual(user.username, 'testuser')

    # ==========================================
    # Test Case 2 ~ Database Involved
    # ==========================================
    def test_user_count(self):
        User.objects.create(username = 'user1')
        User.objects.create(username = 'user2')
        self.assertEqual(User.objects.count(), 2)