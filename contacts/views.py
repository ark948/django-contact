from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView
from contacts.models import ContactEntry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IndexView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("accounts:login")
    context_object_name = "user_contact_list"
    template_name = "contacts/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return ContactEntry.objects.filter(owner__pk=self.request.user.pk)
    
@login_required
def manual_index(request):
    user_contact_list = ContactEntry.objects.filter(owner__pk=request.user.pk)
    context = {
        "item_list": user_contact_list
    }
    return render(request, "contacts/manual_index.html", context=context)