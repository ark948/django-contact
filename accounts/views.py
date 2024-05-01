from django.shortcuts import render

# Create your views here.

def panel_view(request):
    return render(request, "accounts/panel.html")