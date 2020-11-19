from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
   
def services(request):
    return render(request, "services.html")

def contech(request):
    return render(request, "contech.html")

def salon(request):
    return render(request, "salon.html")
