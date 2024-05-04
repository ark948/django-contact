from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView
from contacts.models import ContactEntry
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from contacts.forms import NewContactForm
from contacts.utils import make_new_contact_entry
from django.core.paginator import Paginator
from icecream import ic
ic.configureOutput(includeContext=True)

class IndexView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("accounts:login")
    context_object_name = "user_contact_list"
    template_name = "contacts/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return ContactEntry.objects.filter(owner__pk=self.request.user.pk)
    
@login_required
def manual_index(request):
    user_contact_list = ContactEntry.objects.filter(owner__pk=request.user.pk)
    paginator = Paginator(user_contact_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
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
            contact_object = {
                "title" : form.cleaned_data["title"],
                "first_name" : form.cleaned_data["first_name"],
                "last_name" : form.cleaned_data["last_name"],
                "phone_number" : form.cleaned_data["phone_number"],
                "email" : form.cleaned_data["email"],
                "address" : form.cleaned_data["address"],
                "owner": request.user,
            }
            try:
                try:
                    result = make_new_contact_entry(contact_object)
                except Exception as error_in_getting_result:
                    ic(error_in_getting_result)
                    return redirect("contacts:manual_index")
                try:
                    if result["status"] == True:
                        messages.success(request, "مخاطب جدید افزوده شد.")
                        return redirect("contacts:manual_index")
                    else:
                        ic(result["message"])
                        messages.error(request, "خطای رخ داده است.")
                        return redirect("contacts:manual_index")
                except Exception as error_in_displaying_status:
                    ic(error_in_displaying_status)
                    return redirect("contacts:manual_index")
            except Exception as error:
                ic(error)
                return redirect("contacts:manual_index")
    return render(request, "contacts/manual_new_contact.html", context)