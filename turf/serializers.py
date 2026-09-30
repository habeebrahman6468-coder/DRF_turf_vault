from rest_framework import serializers

class Turfserializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    name = serializers.CharField()

    location = serializers.CharField()

    phone = serializers.IntegerField()

    fee = serializers.IntegerField()

    def validate(self, validated_data):

         fee = validated_data.get("fee")

         if fee<400:

              raise serializers.ValidationError("invalid fee . fee should be >400")

         return validated_data    



class AdminSerializer(serializers.Serializer):

     username =serializers.CharField()

     email = serializers.EmailField()

     password = serializers.CharField()
     




