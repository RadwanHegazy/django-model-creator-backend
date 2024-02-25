from django.urls import path, include

urlpatterns = [
    path('',include('app.apis.urls'))
]
