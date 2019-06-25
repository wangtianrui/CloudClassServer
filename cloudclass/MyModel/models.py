from django.db import models


# Create your models here.

class User(models.Model):
    # 主键为phone
    phone = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    type = models.IntegerField()
    class_number = models.CharField(max_length=20)
    pass_word = models.CharField(max_length=20)
    avatar = models.CharField(max_length=100)
    academy = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20)
