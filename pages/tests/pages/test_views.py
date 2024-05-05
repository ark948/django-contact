from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from accounts.models import CustomUser

# simpletestcase -> since home page does not need database
# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_homepage_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_view(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "صفحه اصلی")

class TestUserLogin(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser()
        self.user.pk = 1
        return super().setUp()
    
    def test_user_was_created(self):
        self.assertEqual(isinstance(self.user, CustomUser), True)
        self.assertEqual(self.user.pk, 1)