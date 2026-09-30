from rest_framework import serializers


class BookingsSerializer(serializers.Serializer):

    customer_name = serializers.CharField()

    contact_no = serializers.CharField()

    turf = serializers.IntegerField()

    reservation_date = serializers.DateField()

    reservation_time = serializers.TimeField(read_only=True)

    duration = serializers.DurationField()



