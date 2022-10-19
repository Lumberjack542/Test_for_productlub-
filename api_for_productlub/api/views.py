from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from .pydent_test import card


class ArticleBrandApiView(viewsets.ModelViewSet):
    queryset = BrandArticleModel.objects.all()
    serializer_class = BrandArticleSerializer


class AddForPydantic(APIView):
    def post(self, request):


        return JsonResponse({"status": "success"})


