from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'webscrap/main.html')
def about(request):
    return render(request,'webscrap/about.html')
def personalize(request):
    return render(request,'webscrap/personalize.html')
def contact(request):
    return render(request,'webscrap/contact.html')