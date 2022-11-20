from django.shortcuts import render, redirect
from .forms import PhoneForm
from .models import ContactsBook
from django.db.models import Q

def homepage(request):
  if request.method == "POST":
    form = PhoneForm(request.POST)
    if form.is_valid():
      form.save()
  people = ContactsBook.objects.all().order_by("name", "profession").values()
  form = PhoneForm()
  return render(request, "home.html", {"form": form, "contacts":people})

def delete(request, id):
  contact= ContactsBook.objects.get(id=id)
  if request.method=="POST":
    contact.delete()
    return(redirect("/"))
  return render(request, "confirm.html", {"contact":contact})

def updatePage(request, id):
  contact= ContactsBook.objects.get(id=id)
  form= PhoneForm(instance=contact)
  form= PhoneForm(request.POST, instance=contact)
  context ={"form":form, "contact": contact}
  return render(request, "update.html",context)

def update(request, id):
  contact = ContactsBook.objects.get(id=id)
  if (request.POST["name"]!="" and request.POST["name"]!=contact.name):
    contact.name = request.POST["name"]
  if (request.POST["profession"]!="" and request.POST["profession"]!=contact.profession):
    contact.profession = request.POST["profession"]
  if (request.POST["telephone1"]!="" and request.POST["telephone1"]!=contact.telephone1):
    contact.telephone1 = request.POST["telephone1"]
  if (request.POST["telephone2"]!="" and request.POST["telephone2"]!= contact.telephone2):
    contact.telephone2 = request.POST["telephone2"]
  contact.save()
  return (redirect("/"))

def searchPage(request):
  people = ContactsBook.objects.all().order_by("name", "profession").values()
  return render(request, "search.html", {"contacts":people})

def searchN(request):
  searched = request.POST.get("search")
  contacts= ContactsBook.objects.filter(Q(name__contains=searched))
  contacts = contacts.order_by("name", "profession").values()
  return render(request, "search.html", {"searched":searched, "contacts":contacts})

def searchT(request):
  searched = request.POST.get("search")
  contacts= ContactsBook.objects.filter(Q(telephone1__contains=searched) | Q(telephone2__contains=searched))
  contacts = contacts.order_by("name", "profession").values()
  return render(request, "search.html", {"searched":searched, "contacts":contacts})

def searchP(request):
  searched = request.POST.get("search")
  contacts= ContactsBook.objects.filter(Q(profession__contains=searched))
  contacts = contacts.order_by("name", "profession").values()
  return render(request, "search.html", {"searched":searched, "contacts":contacts})

def comparePage(request):
  people = ContactsBook.objects.all().order_by("name", "profession").values()
  return render(request, "compare.html", {"contacts":people})

def compare(request):
  searched1 = request.POST.get("search1")
  searched2 = request.POST.get("search2")
  person1= ContactsBook.objects.filter(Q(name__contains=searched1))
  person2= ContactsBook.objects.filter(Q(name__contains=searched2))
  contacts = ContactsBook.objects.all().order_by("name", "profession").values()
  return render(request, "compare.html", {"contacts":contacts, "person1":person1, "person2":person2})
