from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
import os
from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)

@login_required(login_url='/login')
def readLog(request):
    command = 'tail -n 40 /var/log/maillog'
    output = os.popen(command).readlines()
    return render(request,'log.html',{'output':output})

def index(request):
    return render(request,'index.html')

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/maillog")
    return render(request,'login.html',{"form":form})

def logout_view(request):
    logout(request)
    return redirect('/login')
