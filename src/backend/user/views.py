from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserDetails
from .serializers import UserDetailsSerializer, UserSerializer, LoginSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .utils import EmailUtils
from datetime import datetime


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.data["email"], email=serializer.data["email"])
            
            site_url = request.scheme + '://' + request.get_host() + '/set/password/'
            subject = "[ACTION REQUIRED] Set your account password"
            message = f"Hi User,\nYour account has been created for the erp system at {datetime.now()}.\nPlease click on the below link to change your account password.\n'{site_url}\n\nRegards,\nERP Support"
            recipient_list = [serializer.data["email"]]
            EmailUtils.send_email(recipient_list, subject, message)
            
            user.save()
            return Response(serializer.data["email"], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.data["email"], email=serializer.data["email"])
            user.set_password(serializer.data["password"])  # This will hash the password before saving
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserChangePasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.data["email"], email=serializer.data["email"])
            user.set_password(serializer.data["password"])  # This will hash the password before saving
            user.save()
            return Response({'message': 'password updated/changed'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'password updation failed'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': "user doesn't exist"}, status=status.HTTP_401_UNAUTHORIZED)
            if not user_obj.check_password(password):
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            refresh = RefreshToken.for_user(user_obj)
            return Response({
                'user': serializer.data["email"],
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        token = request.POST["refresh_token"]
        print(token)
        try:
            refresh = RefreshToken(token)
            refresh.blacklist()
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)


class UserDetailsInsertData(APIView):
    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"user_email": str(serializer.data['email']), "created": "True"}, status=status.HTTP_201_CREATED)
        return Response({"error":"user details is invalid"}, status=status.HTTP_400_BAD_REQUEST)


class ProtectedView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # Access user information from the request object
        user = request.user

        # Perform some operation requiring authentication
        data = f"Hello, {user.username}! You are authenticated."
        # EmailUtils.send_email(['richardfranklin41@gmail.com'], 'Test Email', 'This is the message for the said test email')
        
        site_url = request.scheme + '://' + request.get_host() + '/set/password/'
        subject = "[ACTION REQUIRED] Set your account password"
        message = f"Hi User,\nYour account has been created for the erp system at {datetime.now()}.\nPlease click on the below link to change your account password.\n'{site_url}\n\nRegards,\nERP Support"
        recipient_list = ['richardfranklin41@gmail.com']
        EmailUtils.send_email(recipient_list, subject, message)

        return Response({"data":"done"}, status=status.HTTP_200_OK)


class LoginRefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.POST["refresh_token"]
        if not refresh_token:
            return Response({'error': 'Request token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh_token = RefreshToken(refresh_token)
            access_token = str(refresh_token.access_token)
        except Exception as e:
            Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                'access':str(access_token),
                'refresh': str(refresh_token),
            }, status=status.HTTP_200_OK)