from django.test import TestCase
from accounts.models import CustomUser
from django.contrib.auth import authenticate

class AccountsCustomUserModel(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username="some_username")
        self.user.first_name = "firstName"
        self.user.last_name = "lastName"
        self.user.email = "somerandom@email.com"
        self.user.full_name = self.user.first_name + " " + self.user.last_name
        self.user.pk = 1
        self.user.set_password("123")
        self.user.save() # this is necessary
        return super().setUp()
    
    def test_user_info(self):
        self.assertEqual(self.user.username, "some_username")
        self.assertEqual(self.user.first_name, "firstName")
        self.assertEqual(self.user.last_name, "lastName")
        self.assertEqual(self.user.email, "somerandom@email.com")
        self.assertEqual(self.user.full_name, "firstName lastName")
        self.assertEqual(self.user.pk, 1)
        self.assertEqual(self.user.check_password("123"), True)

    def test_user_auth(self):
        logged_in = self.client.login(username="some_username", password="123")
        self.assertTrue(logged_in)
    
        