from rest_framework.views import APIView
from zibar import serializers
from zibar import models
from rest_framework.response import Response
from rest_framework import status




class ContactUs(APIView):

    def post(self, request):

        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            full_name = serializer.data.get('full_name')
            email = serializer.data.get('email')
            subject = serializer.data.get('subject')
            content = serializer.data.get('content')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        models.ContactUs.objects.create(full_name=full_name, email=email,subject=subject,  content=content)

        return Response({'status': 'OK'}, status=status.HTTP_200_OK)