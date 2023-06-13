from . forms import RecordForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Record
from django .http import HttpResponse
# Create your views here.
def home(request):
    records=Record.objects.all()
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        # authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have logged in')
            return redirect('/')
        else:
            messages.success(request,'Please check your credentials')
            return redirect('/')
    else:

         return render(request, 'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, ' successfully logouted')
    return redirect('home')

def register(request):
    return render(request, 'register.html')
def detail(request,id):
    records=Record.objects.get(id=id)
    return render(request,"detail.html" ,{'records':records})
def update(request,id):
    records=Record.objects.get(id=id)
    form=RecordForm(request.POST or None,request.FILES, instance=records)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'records':records})