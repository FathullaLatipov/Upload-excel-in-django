from django.shortcuts import render

from rest_framework import generics
from .models import MyModel
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = ProductSerializer
