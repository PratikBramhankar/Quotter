from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ReactSerializer
from .models import React
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class ReactView(APIView):

    def get(self, request):
        data = React.objects.all() 
        if "search" in request.query_params and  request.query_params.get('search'):
            data = data.filter(Q(name__icontains=request.query_params.get('search')) | Q(detail__icontains=request.query_params.get('search'))).all()
        serializer = ReactSerializer(data, many = True)
        return Response(data={'status':'success', 'message':"quotes listing", 'data':serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'status':'success', 'message':"Quote Created", 'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors)
        
class QuoteDetailView(APIView):

    def get(self, request, pk):
        try:
            data = React.objects.get(pk=pk)
            serializer = ReactSerializer(data, partial = True)
            return Response(data={'status':'success', 'message':"quote listing", 'data':serializer.data}, status=status.HTTP_200_OK) 

        except:
            return Response(data={'status':'error', 'message':"quote not found", 'data':[]}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = React.objects.get(pk=pk)
            obj.delete()
            return Response(data={'status':'success', 'message':"Quote Deleted", 'data':[]}, status=status.HTTP_200_OK)        
        
        except:
            return Response(data={'status':'error', 'message':"quote not found", 'data':[]}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        try:
            obj = React.objects.get(pk=pk)
            serializer = ReactSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'status':'success', 'message':"Quote Updated", 'data':serializer.data}, status=status.HTTP_200_OK) 
            
        except:
            return Response(data={'status':'error', 'message':"quote not found", 'data':[]}, status=status.HTTP_400_BAD_REQUEST)
            
        
            
