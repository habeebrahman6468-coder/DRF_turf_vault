from rest_framework import serializers

from datetime import datetime

from django.contrib.auth.models import User

from booking_v2.models import Booking

class SignupSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class BookingSerializer(serializers.ModelSerializer):

  turf = serializers.StringRelatedField()
  
  class Meta:
    
    model = Booking
    
    fields = "__all__"
    
    read_only_fields = ["end_time","created_at"]
    
  def validate(self,validated_data):
    
    reservation_date = validated_data.get("reservation_date")
    
    if reservation_date < datetime.today().date():
      
      raise serializers.ValidationError("invalid booking date. Enter a valid date")
    
    else: 
      
      return validated_data