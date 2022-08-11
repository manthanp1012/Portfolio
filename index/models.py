from statistics import mode
from django.db import models

# Create your models here.


class Contact(models.Model):
    passname = models.CharField(max_length=30)
    passemail = models.EmailField(max_length=30)
    passphone = models.CharField(max_length=30)
    passconcern = models.TextField(max_length=30)

    # name = models.CharField(max_length=30)
    # email = models.EmailField(max_length=30)
    # phone = models.EmailField(max_length=30)
    # concern = models.TextField(max_length=30)
