from django.shortcuts import render

from rest_framework import mixins,generics
from .serializers import ProductSerializer
from .models import Product

class ProductList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer

	def get(self,request):
		return self.list(request)

	def post(self,request):
		return self.create(request)

class ProductDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
	queryset=Product.objects.all()
	serializer_class=ProductSerializer

	def get(self,request,pk):
		return self.retrieve(request)
	def put(self,request,pk):
		return self.update(request)
	def delete(self,request,pk):
		return self.destroy(request)
