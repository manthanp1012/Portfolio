from unicodedata import name
from django.shortcuts import render
from index.models import Contact
from django.core.mail import EmailMultiAlternatives
from portfolio import settings
from email.message import EmailMessage
import smtplib
import ssl
import requests

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def send_mail_contact(mail):
    email_subject = 'Concern Submitted Successfully'
    # html_message = render_to_string('cab/Cab_booked_Student.html')
    email_body = "Your Concern is being Checked out! We will get back to you soon!"
    msg = EmailMultiAlternatives(
        email_subject, email_body, 'patilmanthan51@gmail.com', ['patilmanthan51@gmail.com'])
    # msg.attach_alternative(html_message, "text/html")
    msg.send()
    print("sent success")


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
        send_mail_contact(email)
        # print(obj.name)
    return render(request, 'contact.html')
    # except:
    #     return render(request, 'home.html')
