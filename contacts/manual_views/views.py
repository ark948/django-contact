from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseForbidden
from contacts.models import ContactEntry
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contacts.forms import NewContactForm
from contacts.utils import make_new_contact_entry
from django.core.paginator import Paginator
from icecream import ic
ic.configureOutput(includeContext=True)

@login_required
def index(request):
    user_contact_list = ContactEntry.objects.filter(owner__pk=request.user.pk)
    paginator = Paginator(user_contact_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, "contacts/manual/index.html", context=context)

@login_required
def new_contact(request):
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
    return render(request, "contacts/manual/new_contact.html", context)

@login_required
def delete_contact(request):
    if request.method == "POST":
        item_to_delete = ContactEntry.objects.get(pk=int(request.POST.get("id_to_delete")))
        try:
            if item_to_delete.owner.id == request.user.id:
                item_to_delete.delete()
                messages.info(request, "مخاطب حذف شد.")
        except Exception as error:
            ic(error)
    return redirect("contacts:manual_index")

@login_required
def edit_contact(request):
    # view to get and display the edit form
    context = {}
    if request.method == "POST":
        item_to_edit = ContactEntry.objects.get(pk=int(request.POST.get("id_to_edit")))
        data = {}
        # get data to poulate the form
        data["title"] = item_to_edit.title
        data["first_name"] = item_to_edit.first_name
        data["last_name"] = item_to_edit.last_name
        data["phone_number"] = item_to_edit.phone_number
        data["email"] = item_to_edit.email
        data["address"] = item_to_edit.address
        form = NewContactForm(data=data)
        context["form"] = form
        context["full_name"] = item_to_edit.full_name
        context["item_id"] = item_to_edit.id
        return render(request, "contacts/manual/edit_contact.html", context)
    else:
        return HttpResponse("مخاطبی برای ویرایش یافت نشد.")


@login_required
def process_contact_edit(request):
    if request.method == "POST":
        try:
            form = NewContactForm(request.POST)
        except Exception as form_error:
            ic(form_error)
            return redirect("contacts:manual_index")
        if form.is_valid():
            try:
                item_id = request.POST.get("item_id")
                item = ContactEntry.objects.get(pk=int(item_id))
            except Exception as item_retrieve_error:
                ic(item_retrieve_error)
                return redirect("contacts:manual_index")
            try:
                if item.owner.id != request.user.id:
                    return HttpResponseForbidden
            except Exception as resource_error:
                ic("NOT ALLOWED")
            try:
                item.title = form.cleaned_data["title"]
                item.first_name = form.cleaned_data["first_name"]
                item.last_name = form.cleaned_data["last_name"]
                item.phone_number = form.cleaned_data["phone_number"]
                item.email = form.cleaned_data["email"]
                item.address = form.cleaned_data["address"]
            except Exception as data_update_error:
                ic(data_update_error)
            try:
                item.save()
                messages.success(request, "ویرایش با موفقیت انجام شد.")
                return redirect("contacts:manual_index")
            except Exception as update_process_error:
                ic(update_process_error)
                return redirect("contacts:manual_index")
    return redirect("contacts:manual_index")