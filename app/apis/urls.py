from .views import get, create
from django.urls import path

urlpatterns = [
    path('model/get/',get.GetSupprotedFields),
    path('model/create/',create.CreateModel),
]