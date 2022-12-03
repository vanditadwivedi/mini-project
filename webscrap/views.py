from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Personalize,Tags,jobDetails
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    return render(request,'webscrap/main.html')
def about(request):
    return render(request,'webscrap/about.html')
def personalize(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            print(request)
            email = request.POST.get("email")
            # if email is None:
            #     messages.error(request,"email cannot be empty")
            #     return render(request,'webscrap/personalize.html')
            skill = request.POST.get("skill")
            # if skill is None:
            #     messages.error(request,"skill cannot be empty")
            #     return render(request,'webscrap/personalize.html')
            if Tags.objects.filter(skill = skill).exists():
                request.user.email = request.POST.get("email", "")
                personalize= Personalize(user = request.user,skill=skill)
                personalize.save()
                request.user.save()
                messages.success(request, "Ho gya balle balle")
            else:
                messages.error(request,"we dont have this skill in our database please request this skill")
                return redirect("request_tag")
        else:
            messages.error(request,"Please log in or create account first to personalize")
            return render(request,'webscrap/main.html')
    return render(request,'webscrap/personalize.html')
def contact(request):
    return render(request,'webscrap/contact.html')
def request_tag(request):
    if request.method=='POST':
        #thank=False
        print(request)
        skill = request.POST.get("skill")
        if request.user.is_authenticated:
            tags= Tags(skill=skill,user=request.user)
            tags.save()
            messages.success(request,"we have added this skill we will soon notify you via email")
            return render(request,'webscrap/main.html')

        else:
            messages.error(request,"you should be logged in or have a acount to request tags!")
            
    return render(request,'webscrap/request_tag.html')