from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from bookings.models import Bookings
from bookings.serializer import BookingsSerializer
from turf.models import Turf

# Create your views here.

class BookingListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request):

        qs = Bookings.objects.all() #qs=> pynt => serialzer 

        serializer_instance = BookingsSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = BookingsSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            turf = cleaned_data.get("turf")       # MAIN PART

            turf_object = Turf.objects.get(id =turf)

            cleaned_data["turf"] = turf_object

            Bookings.objects.create(**cleaned_data)       #XXXXXXXXXX

            response_data = {
                                "status": "booked",
                                "message": "Turf booked successfully"
                            }
                    
            return Response(data=response_data)

        else:

            return Response(data=serializer_instance.errors)




        





            

