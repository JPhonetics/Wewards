from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AccountUserSerializer


class AccountUserRegistration(APIView):
    
    def post(self, request):
        serialized = AccountUserSerializer(
            data = request.data
        )
        
        if serialized.is_valid():
            new_user = serialized.save()
            
            return Response(
                AccountUserSerializer(new_user).data,
                status = status.HTTP_201_CREATED
            )
            
        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        

class AccountUserLogin(APIView):
    
    def post(self, request):
        email = request.data.get('email')

        if email:
            email = email.strip().casefold()
        
        user = authenticate(
            username = email,
            password = request.data.get('password')
        )
        
        if not user:
            return Response(
                "Invalid credentials.",
                status = status.HTTP_404_NOT_FOUND
            )
            
        return Response(
           {"user": user.email}, 
           status=status.HTTP_200_OK 
        )