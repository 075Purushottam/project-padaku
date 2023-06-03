from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    return render(request,'product_app/home.html')

def loginPage(request):
    page='login'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not Exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'User password is not Correct')
    context = {'page':page}
    return render(request,'product_app/login_register.html',context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        # print(request.POST.get('username'))
        # print(request.POST.get('password'))
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Error occured during registration')

    return render(request,'product_app/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def productPage(request):
    return render(request,'product_app/product-page.html')

def enquiryPage(request):
    return render(request,'product_app/enquiry.html')