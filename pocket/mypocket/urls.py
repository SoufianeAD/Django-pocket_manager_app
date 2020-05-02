from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginForm, name="loginForm"),
    path('/login/', views.login, name="login"),
    path('/createItemForm/', views.createItemForm, name="createItemForm"),
    path('/listItems/', views.listItems, name="listItems"),
    path('/createItem/', views.createItem, name="createItem"),
]