from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Todo

from .serializers import TodoSerializers


class ListTodo(generics.ListCreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializers
