from rest_framework import serializers



class ContactUsSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    subject = serializers.CharField()
    content = serializers.CharField()