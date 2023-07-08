from django.shortcuts import render,HttpResponse
from connections.models import connect,Contact
from django.contrib import messages
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