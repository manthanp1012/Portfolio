from unicodedata import name
from django.shortcuts import render
from index.models import Contact

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern = request.POST['concern']
        # print(name)
        # print(email)
        # print(phone)
        # print(concern)
        obj = Contact(name=name, email=email,
                      phone=phone, concern=concern)
        obj.save()
        # print(obj.name)
    return render(request, 'contact.html')
