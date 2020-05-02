from django.shortcuts import render
from .models import Item, User

# Create your views here.
def loginForm(request):
    return render(request, 'mypocket/loginForm.html')

def login(request):
    userName = request.POST["userName"]
    password = request.POST["password"]
    if password != "123":
        message = "Username or password incorrect!"
        return render(request, 'mypocket/loginForm.html', {"message": message})
    items = Item.objects.all();
    return render(request, 'mypocket/items.html', {"items": items})

def createItemForm(request):
    return render(request, 'mypocket/CreateItemForm.html')

def listItems(request):
    items = Item.objects.all();
    return render(request, 'mypocket/items.html', {"items": items})

def createItem(request):
    items = Item.objects.all();
    return render(request, 'mypocket/items.html', {"items": items})