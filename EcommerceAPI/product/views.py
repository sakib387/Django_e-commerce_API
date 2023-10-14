from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import Brand,Category,Product
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer


class CategoryView(viewsets.ViewSet):
    quaryset=Category.objects.all()
    def list(self,request):
        serializer=CategorySerializer(self.quaryset,many=True)
        return Response(serializer.data)