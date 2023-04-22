from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from authority.serializers import AuthoritySerializer
from authority.models import Authority

# Create your views here.
class ListAuthorityAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer

class CreateAuthorityAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer

class UpdateAuthorityAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer

class DeleteAuthorityAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer