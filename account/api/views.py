from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SignUpUserView(generics.GenericAPIView):
    def user_signup(request):
        return Response('hello')


class SignInUserView():
    pass


class SignOutUserView():
    pass