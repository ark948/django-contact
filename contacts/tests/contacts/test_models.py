from django.test import TestCase
from contacts.models import ContactEntry
# from django.conf import settings
from accounts.models import CustomUser

# this fails
class ContactEntryTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser()
        self.user.pk = 1
        self.user.username = "user1"
        self.contact = ContactEntry()
        self.contact.owner = self.user
        self.contact.title = "some_title"
        return super().setUp()
    
    def test_user_created(self):
        self.assertEqual(self.user.username, "user1")
        self.assertEqual(isinstance(self.user, CustomUser), True)

    def test_user_got_id(self):
        self.assertEqual(self.user.pk, 1)

    def test_contact_object_created(self):
        self.assertEqual(isinstance(self.contact, ContactEntry), True)

    def test_contact_info(self):
        self.assertEqual(self.contact.owner, self.user)
        self.assertEqual(self.contact.title, "some_title")