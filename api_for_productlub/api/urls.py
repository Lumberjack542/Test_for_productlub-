from .views import *
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('', FileArticleApiview.as_view()),  #add article and file
    path('article', article_obj),

]