<<<<<<< HEAD
from django.conf import settingsfrom django.contrib.auth.models import AbstractUserfrom django.db import modelsclass TodoUser(AbstractUser):    user_name = models.CharField(max_length=64)    first_name = models.CharField(max_length=64)    last_name = models.CharField(max_length=64)    birthday_year = models.PositiveIntegerField(default='0000')    email = models.EmailField(unique=True)
=======
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TodoUser(AbstractUser):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(default='0000')
    email = models.EmailField(unique=True)
>>>>>>> 71cf598206b139ac30a5b8dd15ead79c66e0062a
