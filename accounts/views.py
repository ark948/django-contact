from django.contrib.auth.forms import AuthenticationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages
from accounts.forms import CustomUserCreationForm, ManualLoginForm

# Create your views here.

def panel_view(request):
    if request.user.is_authenticated:
        messages.info(request, "شما وارد سایت شده اید.")
        return redirect("pages:home")
    return render(request, "accounts/panel.html")

def manual_login(request):
    if request.user.is_authenticated:
        messages.info(request, "شما وارد سایت شده اید.")
        return redirect("pages:home")
    info = {}
    if request.method == "POST":
        form = ManualLoginForm(request.POST)
        if form.is_valid():
            info["username"] = form.cleaned_data["username"]
            info["password"] = form.cleaned_data["password"]
            user = authenticate(request, username=info["username"], password=info["password"])
            if user is not None:
                try:
                    login(request, user)
                    messages.success(request, "ورود با موفیت.")
                except Exception as login_error:
                    messages.error(request, "خطا در فرایند ورود.")
                    return redirect("accounts:panel")
            else:
                messages.error(request, "اطلاعات شما یافت نشد.")
                return redirect("accounts:panel")
        else:
            messages.error(request, "خطا در فرم.")
            return redirect("accounts:panel")
    else:
        form = ManualLoginForm()
    return render(request, "registration/manual/manual_login.html", {"form": form})

def manual_logout(request):
    try:
        logout(request)
        messages.success(request, "خروج با موفقیت.")
    except Exception as logout_error:
        messages.error(request, "خطا در فرایند خروج.")
    return redirect("pages:home")

class MyLoginView(LoginView):
    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            messages.info(request, "شما وارد سایت شده اید.")
            return redirect("pages:home")
        return super().get(request, *args, **kwargs)
    template_name = "registration/login.html"

class MyLogoutView(LogoutView):
    def post(self, request: WSGIRequest, *args, **kwargs) -> TemplateResponse:
        messages.success(request, "با موفقیت از سایت خارج شدید.")
        return super().post(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"