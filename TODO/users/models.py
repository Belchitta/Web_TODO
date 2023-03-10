from django.contrib.auth.models import AbstractUser
from django.db import models


<<<<<<< HEAD
# class TodoUser(AbstractUser):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     birthday_year = models.PositiveIntegerField(default='0000')
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return f'{self.first_name} | {self.last_name}'

class TodoUser(AbstractUser):
    email = models.EmailField(unique=True)
=======
class TodoUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(default='0000')
    email = models.EmailField(unique=True)
<<<<<<< HEAD

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'
=======
>>>>>>> parent of b0be2de... Lesson_9_Done
>>>>>>> main
