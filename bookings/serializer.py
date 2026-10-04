from rest_framework import serializers

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



