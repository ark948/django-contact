from django import forms

class NewContactForm(forms.Form):
    title = forms.CharField(max_length=200, label="عنوان")
    first_name = forms.CharField(max_length=100, label="نام")
    last_name = forms.CharField(max_length=150, label="نام خانوادگی")
    phone_number = forms.CharField(max_length=40, label="شماره تماس")
    email = forms.EmailField(label="ایمیل")
    address = forms.CharField(label="آدرس")