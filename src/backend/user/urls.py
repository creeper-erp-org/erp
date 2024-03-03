from django.urls import path
from .views import UserDetailsInsertData,  UserRegistrationView, LoginView, LogoutView, ProtectedView, UserSetPasswordView


urlpatterns = [
     path('register/', UserRegistrationView.as_view(), name='register'),
     path('login/', LoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('user/create/', UserDetailsInsertData.as_view(), name='createuserapi'),
     path('dashboard/', ProtectedView.as_view(), name='logout'),
     path('set/password/', UserSetPasswordView.as_view(), name='setpassword')
]
