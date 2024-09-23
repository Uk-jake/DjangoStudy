from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("get/", views.showGetDescription),
    path("get/<str:itemid>", views.getItem),
    
    path('querystring', views.queryString),
]
