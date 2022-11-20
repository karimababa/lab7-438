from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("updatePage/<int:id>", views.updatePage, name="updatePage"),
    path("updatePage/update/<int:id>", views.update, name="update"),
    path("searchPage", views.searchPage, name="searchPage"),
    path("searchN", views.searchN, name="searchN"),
    path("searchT", views.searchT, name="searchT"),
    path("searchP", views.searchP, name="searchP"),
    path("comparePage", views.comparePage, name="comparePage"),
    path("compare", views.compare, name="compare")
]