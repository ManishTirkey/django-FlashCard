from django.urls import path
from .import views

app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
# path("<slug:slug>/", views.index, name=("index")),
    path("add/", views.add, name="add"),
    path("sub/", views.sub, name="sub"),
    path("mult/", views.mult, name="mult"),
    path("div/", views.div, name="div"),
]