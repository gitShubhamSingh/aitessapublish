import os
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import createEmbeddings
from . import models
from . import serializers
from . import chat



class IndexChat(APIView):

    def get(self, request):
        
        return Response({
            "status":status.HTTP_200_OK,
            "data":"Get Method Called"
        })

    def post(self, request):
        filePath = os.path.join(settings.BASE_DIR, 'uploads')
        for file in os.listdir(filePath):
            if file == "spice.pdf":
                fileAddress = filePath+"/"+file
                print(fileAddress)
                createEmbeddings.createEmbeddingsForPdf(pdfId="01",pdfPath=fileAddress)

        return Response({
            "status":status.HTTP_200_OK,
            "data":"Post Method Called"
        })
    

class AskChat(APIView):
    def get(self, request):
        return Response({
            "status":status.HTTP_405_METHOD_NOT_ALLOWED,
            "data":"Get Method Not allowed"
        })
    
    def post(self, request):
        chatObject = chat.build_chat()
        result = chatObject.run("who is shahrukh khan ?")
        # print(result)
        return Response({
            "status":status.HTTP_200_OK,
            "data":result
        })
    
    
    
    