from django.urls import path
from .views import UserDetailsInsertData


urlpatterns = [
     path('user/create/', UserDetailsInsertData.as_view(), name='create-user-api')
]
