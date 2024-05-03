from django.db import models
from accounts.models import CustomUser
from django.conf import settings
from django.urls import reverse

# Create your models here.

class ContactEntry(models.Model):
    title = models.CharField("Entry title",null=False, blank=False, max_length=200)
    first_name = models.CharField("First Name", null=True, blank=True, max_length=100)
    last_name = models.CharField("Last Name", null=True, blank=True, max_length=150)
    phone_number = models.CharField("Phone/Cell Number", null=True, blank=True, max_length=40)
    email = models.EmailField("Email Address", null=True, blank=True)
    address = models.TextField("Address", null=True, blank=True)
    date_created = models.DateTimeField("Created on", auto_now_add=True)
    last_modified = models.DateField("Modified on", auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"<Contact for {self.owner} - {self.id}>"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("contacts:details", kwargs={"pk": self.pk})
