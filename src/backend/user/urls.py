from django.urls import path
from .views import UserDetailsInsertData,  UserRegistrationView, LoginView, LogoutView, ProtectedView, UserSetPasswordView, LoginRefreshView, UserChangePasswordView


urlpatterns = [
     path('register/', UserRegistrationView.as_view(), name='register'),
     path('login/', LoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('user/create/', UserDetailsInsertData.as_view(), name='createuserapi'),
     path('dashboard/', ProtectedView.as_view(), name='logout'),
     path('set/password/', UserSetPasswordView.as_view(), name='setpassword'),
     path('login/refresh/', LoginRefreshView.as_view(), name='loginrefresh'),
     path('change/password/', UserChangePasswordView.as_view(), name='changepassword')
]