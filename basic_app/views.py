from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.

def register(request):

    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"New Account Created:{username}")
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")


    form=NewUserForm
    return render(request,'register.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.info(request,'Logged Out Successfully')
    return redirect('home')

def login_request(request):

    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request,'Invalid Username and Password')
        else:
            messages.error(request,"Invalid")
    form=AuthenticationForm
    return render(request,'login.html',{'form':form})
