from django.urls import path
from .views import UserDetailsInsertData,  UserRegistrationView, LoginView, LogoutView, ProtectedView


urlpatterns = [
     path('register/', UserRegistrationView.as_view(), name='register'),
     path('login/', LoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('user/create/', UserDetailsInsertData.as_view(), name='create-user-api'),
     path('dashboard/', ProtectedView.as_view(), name='logout'),

]
