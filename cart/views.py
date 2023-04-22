from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from cart.serializers import CartSerializer
from cart.models import Cart

# Create your views here.
class ListCartAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CreateCartAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class UpdateCartAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DeleteCartAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer