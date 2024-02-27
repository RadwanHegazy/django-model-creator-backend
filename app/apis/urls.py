from .views import get, create
from django.urls import path

urlpatterns = [
    path('model/get/',get.GetSupprotedFields),
    path('model/get/<str:model_id>/',get.ViewDjModel),
    path('model/create/',create.CreateModel),
]