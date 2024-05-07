from django.urls import path, include
from contacts.manual_views.views import index, new_contact, delete_contact, edit_contact, process_contact_edit, download_csv, quick_new_contact


app_name = "contacts"

urlpatterns = [
    path("manual-index", index, name="manual_index"),
    path("manual-new-contact", new_contact, name="manual_new_contact"),
    path("manual-delete-contact", delete_contact, name="manual_delete_contact"),
    path("manual-edit-contact", edit_contact, name="manual_edit_contact"),
    path("process-contact-edit", process_contact_edit, name="process_contact_edit"),
    path("download-csv", download_csv, name="download_csv"),
    path("quick-new-contact", quick_new_contact, name="quick_new_contact"),
]