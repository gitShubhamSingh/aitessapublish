from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.conf import settings



class Index(APIView):

    def get(self, request, format=None):
        pass
      
    
    def post(self, request, format=None):
      
        serializer = serializers.ContactSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
         
            # serializer.save()
            # email = EmailMessage(
            #     subject="Subject",
            #     body="body",
            #     to=["ptcsam78@gmail.com"]
            # )
            # email.content_subtype = "html"
            # email.body = "Email Body"
            # email.send()
            data = {
                "name":serializer.validated_data['name'],
                "cName":serializer.validated_data['companyName'],
                "email":serializer.validated_data['email'],
                "additionalDetails":serializer.validated_data['additionalDetails']
            }
            from . import utils 
            utils.Util.send_email(data)


            return Response(
                {
                    "statusCode":status.HTTP_201_CREATED,
                    "response":"Data Saved"
                }
            )
        return Response(
            {
                "statusCode":status.HTTP_400_BAD_REQUEST,
                "response":"Error while saving Data"
            }
        )