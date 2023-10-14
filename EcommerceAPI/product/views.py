from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
# Create your views here.
from .models import Brand,Category,Product
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer


class CategoryView(viewsets.ViewSet):
    quaryset=Category.objects.all()
    @extend_schema(responses=CategorySerializer)
    def list(self,request):
        serializer=CategorySerializer(self.quaryset,many=True)
        return Response(serializer.data)

class BrandView(viewsets.ViewSet):
    quaryset=Brand.objects.all()
    @extend_schema(responses=BrandSerializer)
    def list(self,request):
        serializer=BrandSerializer(self.quaryset,many=True)
        return Response(serializer.data)
    
class ProductView(viewsets.ViewSet):
    quaryset=Product.objects.all()
    @extend_schema(responses=ProductSerializer)
    def list(self,request):
        serializer=ProductSerializer(self.quaryset,many=True)
        return Response(serializer.data)