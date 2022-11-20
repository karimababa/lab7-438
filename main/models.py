from django.db import models

# Create your models here.
class ContactsBook(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    telephone1 = models.IntegerField(max_length=7)
    telephone2 = models.IntegerField(max_length=7)