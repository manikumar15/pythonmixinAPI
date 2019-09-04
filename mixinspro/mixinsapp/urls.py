from django.conf.urls import url
from rest_framework import routers
from .views import ProductList,ProductDetail

urlpatterns = [
	url(r'^product/$',ProductList.as_view()),
	url(r'^product/(?P<pk>[0-9]+)',ProductDetail.as_view()),

]