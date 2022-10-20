from django.db import models

# Create your models here.


class BrandArticleModel(models.Model):
    brand = models.CharField(max_length=250)
    article = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=350, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)

    def __str__(self):
        return f"{self.brand}"


class ArticleFile(models.Model):
    article = models.CharField(max_length=250, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d/', null=True,blank=True)
