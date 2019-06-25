from django.db import models


# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    # 主键为phone
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    type = models.IntegerField(max_length=5)
    class_number = models.CharField(max_length=20)
    pass_word = models.CharField(max_length=20)
    avatar = models.CharField(max_length=100)
    academy = models.CharField(max_length=20)
