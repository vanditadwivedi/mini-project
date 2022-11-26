from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
    if  request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username , password=password)
        if user is not None:
            login(request, user)
            return render(request,'webscrap/main.html')
             # Redirect to a success page.
    
        else:
            messages.success(request,("there was error in login please try again! :[ "))
            return render(request,'members/login.html')
             # Return an 'invalid login' error message.
    else:
        return render(request,'members/login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request,("you were succsessfully loged out! "))
    return redirect('index')


def signup_user(request):
    if  request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("registered successfull!!:>"))
            return redirect('index')
    else:
        form=UserCreationForm()
    return render(request,'members/signup.html',{'form':form})