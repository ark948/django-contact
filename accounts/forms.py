from django.contrib.auth.forms import UserChangeForm, UserCreationForm
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