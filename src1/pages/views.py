from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request): # *args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", {})

def contact_view(request):
    return render(request, "contact.html")


def about_view(request):

    return render(request, "about.html")


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")