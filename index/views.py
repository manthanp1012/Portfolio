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
    try:
        if request.method == 'POST':
            name = request.POST['passname']
            email = request.POST['passemail']
            phone = request.POST['passphone']
            concern = request.POST['passconcern']
            # print(name)
            # print(email)
            # print(phone)
            # print(concern)
            obj = Contact(passname=name, passemail=email,
                          passphone=phone, passconcern=concern)
            obj.save()
            # print(obj.name)
        return render(request, 'contact.html')
    except:
        return render(request, 'home.html')
