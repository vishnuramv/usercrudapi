from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView
from .serializers import UserSerializer
from .models import User

class ListUserAPIView(ListAPIView):
    """This endpoint list all of the available users from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUserAPIView(RetrieveAPIView):
    """This endpoint allows for retrieve a specific user by passing in the id from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserAPIView(CreateAPIView):
    """This endpoint allows for creation of a user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific user by passing in the id of the user to update"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific user from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
