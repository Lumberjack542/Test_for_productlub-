import pandas as pd
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
import json


class FileArticleApiview(generics.ListCreateAPIView):
    queryset = ArticleFile.objects.all()
    serializer_class = FileArticleSerializer


def get_data_from_wb():
    url = "https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json"
    response = requests.get(url)
    data = response.json()
    return data


@api_view(['GET'])
def article_obj(request):
    if request.method == 'GET':
        d = ArticleFile.objects.all()
        serializer = FileArticleSerializer(d, many=True)
        article = JsonResponse(serializer.data, safe=False)
        article = article.content
        article = json.loads(article.decode())

        for i in range(len(article)):
            if dict(article[i])['article'] == str(get_data_from_wb()['nm_id']):
                if not BrandArticleModel.objects.filter(brand=get_data_from_wb()['selling']['brand_name'], article=get_data_from_wb()['nm_id'],
                                                        title=get_data_from_wb()['imt_name']).exists():
                    BrandArticleModel.objects.create(brand=get_data_from_wb()['selling']['brand_name'], article=get_data_from_wb()['nm_id'],
                                                     title=get_data_from_wb()['imt_name'])
                    print('save')
        return Response(serializer.data, )


class BrandArticleTitleApiView(generics.ListAPIView):
    queryset = BrandArticleModel.objects.all()
    serializer_class = BrandArticleSerializer


def clear_data():
    BrandArticleModel.objects.all().delete()
    ArticleFile.objects.all().delete()











