from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "Resto_app/home_app.html", {})