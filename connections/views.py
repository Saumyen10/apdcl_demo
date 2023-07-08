from django.shortcuts import render,HttpResponse,redirect
from connections.models import connect,Contact
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')
def connection(request):
    return render(request, 'connection.html')
def about(request):
    return render(request, 'about.html')
def search(request):
    return render(request, 'search.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        issue = request.POST.get('issue')
        contact = Contact (name = name, email = email, phone = phone, issue = issue)
        contact.save()
        messages.success(request, "Your complaint/query has been sent!")
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email is already in used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request,"Name is already in used.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account created successfully!!!")
                return redirect('register')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
    else:
        #method="GET"  
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')