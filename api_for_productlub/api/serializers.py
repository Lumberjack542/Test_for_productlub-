from rest_framework import serializers
from .models import *
from .pydent_test import card


class BrandArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandArticleModel
        fields = '__all__'

