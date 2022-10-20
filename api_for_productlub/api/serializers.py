from rest_framework import serializers
from .models import *


class BrandArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandArticleModel
        fields = "__all__"


class FileArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFile
        fields = ['article', 'file']

