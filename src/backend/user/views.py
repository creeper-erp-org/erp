from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserDetailsSerializer
from rest_framework import status


class UserDetailsInsertData(APIView):
    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
