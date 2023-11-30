from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client():
    subject = "Subject"
    message = "Message                      "
    from_email = settings.EMAIL_HOST_USER
    reciever_email = ["ptcsam74@gmail.com"]
    send_mail(subject, message, from_email, reciever_email)


class Index(APIView):

    def get(self, request, format=None):
        pass
      
    
    def post(self, request, format=None):
        print(request.data['name'])
        serializer = serializers.ContactSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # email = EmailMessage(
            #     subject="Subject",
            #     body="body",
            #     to=["ptcsam78@gmail.com"]
            # )
            # email.content_subtype = "html"
            # email.body = "Email Body"
            # email.send()
            send_mail_to_client()

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