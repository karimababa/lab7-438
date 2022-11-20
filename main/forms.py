from django import forms
from .models import ContactsBook

class PhoneForm(forms.ModelForm):

  class Meta:
    model = ContactsBook
    fields = ('name','profession','telephone1','telephone2')