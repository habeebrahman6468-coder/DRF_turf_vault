from django.shortcuts import render
from django.contrib.auth.models import User 

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import authentication,permissions
from bookings.models import Turf

from bookings.serializers import Turfserializer,AdminSerializer

# Create your views here.


class TurfCreateListView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request):

        qs =Turf.objects.all()

        serializer_instance = Turfserializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = Turfserializer(data=form_data)

        if serializer_instance.is_valid():

           cleaned_data = serializer_instance.validated_data

           Turf.objects.create(**cleaned_data)

           return Response(data=serializer_instance.validated_data)


class TurfRetrieveUpdateDelete(APIView):

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_instance = Turfserializer(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instance = Turfserializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Turf.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance =AdminSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)



            





      

        












