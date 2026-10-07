from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from turf.models import Turf


from booking_v2.serializer import SignupSerializer,BookingSerializer
from booking_v2.models import Booking

from datetime import datetime,timedelta,time

# Create your views here.


class SignupView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = SignupSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data =serializer_instance.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_inst = SignupSerializer(user_object)



            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_instance.errors)


class BookingListCreateiew(APIView):

  authentication_classes = [authentication.BasicAuthentication]

  permission_classes = [permissions.IsAuthenticated]
  
  def get(Self,requset):
    
    qs = Booking.objects.all()
    
    serializer_instance = BookingSerializer(qs,many=True)
    
    return Response(data=serializer_instance.data)
  
  # def post(self,request):

  #       form_data = request.data

  #       serialzer_instance = BookingSerializer(data=form_data)

  #       if serialzer_instance.is_valid():

  #           cleaned_data = serialzer_instance.validated_data

  #           turf = cleaned_data.get("turf")

  #           reservation_date = cleaned_data.get("reservation_date")      #turf ID => serializer => Booking

  #           reservation_time = cleaned_data.get("reservation_time")

  #           duration = cleaned_data.get("duration")

  #           start_datetime = datetime.combine(reservation_date,reservation_time)

  #           end_datetime = start_datetime + duration

  #           end_time = end_datetime.time()

  #           existing_bookings = Booking.objects.filter(turf=turf,reservation_date=reservation_date,reservation_time__lt=end_time,end_time__gt=reservation_time).exists()

  #           if existing_bookings:

  #               return Response(data={"error":" Turf is already booked during the selected time "})

  #           cleaned_data["end_time"] = end_time

  #           new_booking = Booking.objects.create(**cleaned_data)

  #           serialzer_instance = BookingSerializer(new_booking)

  #           return Response(data=serialzer_instance.data)

  #       else:

  #           return Response(data=serialzer_instance.errors)

  def post(self, request):

    form_data = request.data

    serializer_instance = BookingSerializer(data=form_data)

    if serializer_instance.is_valid():

        cleaned_data = serializer_instance.validated_data

        # Get turf ID from request
        turf_id = request.data.get("turf")

        # Get the actual Turf object
        turf = Turf.objects.get(id=turf_id)

        reservation_date = cleaned_data.get("reservation_date")     #MODIFIED because of implemented =>Serializer(stringrelatedfield)
        reservation_time = cleaned_data.get("reservation_time")     # Turf ID => manually get Turf object => Booking => shows the turf name in response data
        duration = cleaned_data.get("duration")

        start_datetime = datetime.combine(
            reservation_date,
            reservation_time
        )

        end_datetime = start_datetime + duration

        end_time = end_datetime.time()

        existing_bookings = Booking.objects.filter(
            turf=turf,
            reservation_date=reservation_date,
            reservation_time__lt=end_time,
            end_time__gt=reservation_time
        ).exists()

        if existing_bookings:
            return Response({
                "error": "Turf is already booked during the selected time"
            })

        cleaned_data["turf"] = turf
        cleaned_data["end_time"] = end_time

        new_booking = Booking.objects.create(**cleaned_data)

        serializer_instance = BookingSerializer(new_booking)

        return Response(data=serializer_instance.data)

    else:

        return Response(data=serializer_instance.errors)
  

# class BookingRetrieveUpdateDeleteView(APIView):

#     def get(self,request,pk=None):

#         qs = Booking.objects.get(id=pk)                        # FIRST IMPLEMENTED METHOD for get,put and delete

#         serializer_instance = BookingSerializer(qs)

#         return Response(data=serializer_instance.data)


class BookingRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class= BookingSerializer

    queryset = Booking.objects.all()


      
            


