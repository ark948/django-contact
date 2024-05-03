from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django import forms
from accounts.models import CustomUser

# in admin interface
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# in user sign up
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("full_name", )
        
password_help_text: str = f"رمزعبور باید از ترکیبی از حروف انگلیسی کوچک، بزرگ، اعداد، و حداقل یک نماد باشد.\n رمزعبور می بایست حداقل 8 کاراکتر باشد."
email_error_message: dict = {"required": "این فیلد نمی تواند خالی باشد.", "invalid": "فرمت آدرس وارد شده صحیح نمی باشد."}

class ManualLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری", max_length=200, required=True,)
    password = forms.CharField(label="رمزعبور", required=True, widget=forms.PasswordInput)
    
    