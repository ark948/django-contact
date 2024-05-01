from django.urls import path, include
from accounts import views

# app_name will effect url tag in templates e.g. {% url 'polls:detail' question.id %}
app_name = "accounts"
urlpatterns = [
    path("panel/", views.panel_view, name="panel"),
]