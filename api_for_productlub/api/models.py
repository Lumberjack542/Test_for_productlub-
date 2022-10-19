from django.db import models

# Create your models here.


class BrandArticleModel(models.Model):
    brand = models.CharField(max_length=250)
    article = models.CharField(max_length=250, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
