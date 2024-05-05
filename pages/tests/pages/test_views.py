from django.test import TestCase, SimpleTestCase
from django.urls import reverse

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