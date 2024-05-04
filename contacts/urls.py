from django.urls import path, include
from contacts import views


app_name = "contacts"

urlpatterns = [
    path("manual-new-contact", views.manual_new_contact, name="manual_new_contact"),
    path("manual-index", views.manual_index, name="manual_index"),
    path("", views.IndexView.as_view(), name="index"),
]