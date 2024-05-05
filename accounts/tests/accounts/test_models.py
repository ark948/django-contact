from django.test import TestCase
from accounts.models import CustomUser

class AccountsCustomUserModel(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser()
        self.user.username = "some_username"
        self.user.first_name = "firstName"
        self.user.last_name = "lastName"
        self.user.email = "somerandom@email.com"
        self.user.full_name = self.user.first_name + " " + self.user.last_name
        self.user.id = 1
        return super().setUp()
    
    def test_user_info(self):
        self.assertEqual(self.user.username, "some_username")
        self.assertEqual(self.user.first_name, "firstName")
        self.assertEqual(self.user.last_name, "lastName")
        self.assertEqual(self.user.email, "somerandom@email.com")
        self.assertEqual(self.user.full_name, "firstName lastName")
        self.assertEqual(self.user.id, 1)
        