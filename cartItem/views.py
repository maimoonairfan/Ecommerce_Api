from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from cartItem.serializers import CartSerializer
from cartItem.models import CartItem

# Create your views here.
class ListCartItemAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer

class CreateCartItemAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer

class UpdateCartItemAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer

class DeleteCartItemAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer