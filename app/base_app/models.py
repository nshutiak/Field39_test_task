from django.db import models
from django.contrib.auth.models import AbstractUser


class Userdata(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'User data'
        verbose_name_plural = 'User data'
        db_table = 'user_data'


class User(AbstractUser):
    form_access = models.BooleanField(default=True)

    class Meta:
        db_table = "user"