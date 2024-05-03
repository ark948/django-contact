from django.urls import path, include
from accounts import views

# app_name will effect url tag in templates e.g. {% url 'polls:detail' question.id %}
# django's builtin auth for login and logout
# accounts urls for signup
# both need to be included
app_name = "accounts"

urlpatterns = [
    path("panel/", views.panel_view, name="panel"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("manual-login", views.manual_login, name="manual_login"),
    path("manual-logout", views.manual_logout, name="manual_logout"),
    path("", views.home, name="home"),
]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']