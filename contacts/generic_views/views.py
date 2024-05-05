from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView
from contacts.models import ContactEntry
from django.contrib.auth.mixins import LoginRequiredMixin
from icecream import ic
ic.configureOutput(includeContext=True)

class IndexView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("accounts:login")
    context_object_name = "user_contact_list"
    template_name = "contacts/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return ContactEntry.objects.filter(owner__pk=self.request.user.pk)
