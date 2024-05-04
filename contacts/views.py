from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView
from contacts.models import ContactEntry
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from contacts.forms import NewContactForm

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

@login_required
def manual_new_contact(request):
    context = {
        "form": NewContactForm()
    }
    if request.method == "POST":
        form = NewContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            try:
                new_contact = ContactEntry()
                new_contact.title = title
                new_contact.first_name = first_name
                new_contact.last_name = last_name
                new_contact.phone_number = phone_number
                new_contact.email = email
                new_contact.address = address
                new_contact.owner = request.user
                new_contact.save()
                messages.success(request, "مخاطب جدید افزوده شد.")
                return redirect("contacts:manual_index")
            except Exception as error:
                print("\n", error)
                messages.error(request, "خطا در افزودن مخاطب")
                return redirect("contacts:manual_index")
    return render(request, "contacts/manual_new_contact.html", context)