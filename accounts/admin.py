from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # fields to be used in displaying the user model
    list_display = ["username", "email", "is_staff"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": ["full_name"]
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": ["full_name"]
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)