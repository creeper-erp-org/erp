from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserDetailsSerializer
import json


class ListUsers(APIView):
    def get(self, request):
        queryset = UserDetails.objects.all()
        # print(queryset)
        serializer  = UserDetailsSerializer(queryset, many = True)
        return Response(serializer.data)
    

