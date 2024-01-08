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
from dotenv import load_dotenv
load_dotenv()
from django.http import StreamingHttpResponse

class IndexChat(APIView):

    def get(self, request):
        
        return Response({
            "status":status.HTTP_200_OK,
            "data":"Get Method Called"
        })

    def post(self, request):
        filePath = os.path.join(settings.BASE_DIR, 'uploads')
        for file in os.listdir(filePath):
            if file == "aitessaDocs.pdf":
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
        # Building the chat module
        chatObject = chat.build_chat()

    
        # Calculating Query embedding 
        try:
            querryEmbeddingScore = createEmbeddings.createEmbeddingForQuerryAndGetScore(request.data['user'])
        except Exception as e:
            print('----')
            querryEmbeddingScore ="timeout"
        if querryEmbeddingScore == "timeout":

            def streamTimeout(myString):
                yield myString
            
            timeoutObject = streamTimeout("Text Embedding Ada Timeout")

            return StreamingHttpResponse(timeoutObject)

        elif querryEmbeddingScore > 0.78:  
            result=""
            
            # result = chatObject.run(request.data['user'])
            try:
                streamObj =  chatObject.stream(request.data['user'])
            except Exception as e:
                print(str(e))
            # return Response({
            #     "role":"assistant",
            #     "content":streamObj
            # })
            return StreamingHttpResponse(streamObj)
               
        else: 
            result="Querry is Not Relevant to Ai Tessa."

            return StreamingHttpResponse(result)
    
    
    
    