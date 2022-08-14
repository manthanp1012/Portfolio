import imp
from unicodedata import name
from django.shortcuts import render
from index.models import Contact
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def mail_sent(mail):
    send_mail(
        'Hi here',
        'Here is the message.',
        'patilmanthan51@gmail.com',
        ['manthanpatil912@gmail.com'],
        fail_silently=False,
    )


def contact(request):
    # try:
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
        mail_sent(email)

        # print(obj.name)
    return render(request, 'contact.html')
    # except:
    #     return render(request, 'home.html')
