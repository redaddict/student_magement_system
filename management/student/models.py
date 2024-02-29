from django.db import models


class Details(models.Model):
    stu_id = models.IntegerField()
    name = models.CharField(max_length=100)
    mob = models.IntegerField(null=True)
    city = models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    year = models.IntegerField()
    course =models.CharField(max_length=100)
