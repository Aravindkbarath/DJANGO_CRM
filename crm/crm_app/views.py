from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signUpForm,addRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been successfully Logged in")
            return redirect('home')
        else:
            messages.success(request,"An error occured please try again...")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})
        

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been successfully registered.")
            return redirect('home')
    else:
        form = signUpForm()
        return render(request,'signUp.html',{'form':form})
    return render(request,'signUp.html',{'form':form})

def add_record(request):
    form = addRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Record Added.")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You must have logged in to Add Record.")
        return redirect('home')
    
def edit_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = addRecordForm(request.POST or None,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated.")
            return redirect('home')
        return render(request,'edit_record.html',{'form':form,'recordId':record.id})
    else:
        messages.success(request,"You must have logged in to update record.")
        return redirect('home')

def delete_record(request,pk):
    print("hi")
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request,"Record Deleted")
        return redirect('home')
    else:
        messages.success(request,"You must have logged in to delete record.")
        return redirect('home')