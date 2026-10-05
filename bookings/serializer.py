from rest_framework import serializers

from datetime import datetime

from turf.models import Turf


class BookingsSerializer(serializers.Serializer):

    customer_name = serializers.CharField()

    contact_no = serializers.CharField()

    turf = serializers.PrimaryKeyRelatedField(
        queryset=Turf.objects.all()
    )

    reservation_date = serializers.DateField()

    reservation_time = serializers.TimeField(read_only=True)

    duration = serializers.DurationField()

    def validate(self, validated_data):

        reservation_date = validated_data.get("reservation_date")

        if reservation_date < datetime.today().date():
            raise serializers.ValidationError("Invalid date")

        return validated_data

    

    



        
    



