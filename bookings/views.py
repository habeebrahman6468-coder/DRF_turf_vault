from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from bookings.models import Bookings
from bookings.serializer import BookingsSerializer

# Create your views here.

class BookingListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request):

        qs = Bookings.objects.all() #qs=> pynt => serialzer 

        serializer_instance = BookingsSerializer(qs,many=True)

        return Response(data=serializer_instance.data)