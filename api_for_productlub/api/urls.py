from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', ArticleBrandApiView)

urlpatterns = [
    #path('add', AddFileApiView.as_view()),
    path('', include(router.urls)),
    path('123/', AddForPydantic.as_view())
]