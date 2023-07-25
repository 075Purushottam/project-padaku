from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product
from .forms import EnquiryForm, FeedbackForm

def home(request):
    products = Product.objects.all()
    form = EnquiryForm()
    fform = FeedbackForm()
    
    if request.method == 'POST' and 'enquiryform' in request.POST:
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry Submited Successfully')
            return redirect('home')
        else:
            messages.error(request,'Fill enquiryform`s all fields Properly')

    if request.method == 'POST' and 'feedbackform' in request.POST:
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            fform.save()
            messages.success(request, 'Feedback Submited Successfully')
            return redirect('home')
        else:
            messages.error(request,'Fill feedbackform`s all fields Properly')
    
    for prod in products:
        prod.description = prod.description[:60]
    
    
    context = {'products':products,'form':form , 'fform':fform}
    return render(request,'product_app/home.html',context) 

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

def productPage(request,pk):
    products = Product.objects.all()
    product = Product.objects.get(id=pk)
    features = product.features_set.all()
    context = {'product':product,'features':features,'products':products}
    return render(request,'product_app/product-page.html',context)

def enquiryPage(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submited Successfully')
            return redirect('home')
        else:
            messages.error(request,'Fill all fields Properly')
    context = {'form':form}
    return render(request,'product_app/enquiry.html',context)

def aboutPage(request):
    return render(request,'product_app/about.html')
