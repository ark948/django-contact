from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.

class PanelPageTest(SimpleTestCase):
    def test_accounts_home_page_url(self):
        response = self.client.get("/accounts/")
        self.assertRedirects(response, "/accounts/panel/")

    def test_panel_page_url(self):
        response = self.client.get("/accounts/panel/")
        self.assertEqual(response.status_code, 200)

    def test_panel_page_view(self):
        response = self.client.get(reverse("accounts:panel"))
        self.assertTemplateUsed(response, "accounts/panel.html")
        self.assertContains(response, "خوش آمدید.")

class CustomLoginViewTest(TestCase):
    def test_custom_login_view_url(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

