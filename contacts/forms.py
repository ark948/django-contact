from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, HTML, Fieldset, Layout

class NewContactForm(forms.Form):
    title = forms.CharField(max_length=200, label="عنوان:", required=True)
    first_name = forms.CharField(max_length=100, label="نام:", required=False)
    last_name = forms.CharField(max_length=150, label="نام خانوادگی:", required=False)
    phone_number = forms.CharField(max_length=40, label="شماره تماس:", required=False)
    email = forms.EmailField(label="ایمیل:", required=False)
    address = forms.CharField(label="آدرس:", required=False)

class QuickNewContactForm(forms.Form):
    title = forms.CharField(max_length=200, label="عنوان:", required=True)
    phone_number = forms.CharField(max_length=150, label="شماره تماس:", required=False)