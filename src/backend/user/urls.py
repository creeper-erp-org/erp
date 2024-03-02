from django.urls import path
from .views import ListUsers

urlpatterns = [
     path('user/create/', ListUsers.as_view())
]
