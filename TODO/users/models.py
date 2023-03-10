from django.contrib.auth.models import AbstractUser
from django.db import models


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
# class TodoUser(AbstractUser):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     birthday_year = models.PositiveIntegerField(default='0000')
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return f'{self.first_name} | {self.last_name}'

<<<<<<< HEAD
=======
class TodoUser(AbstractUser):
    email = models.EmailField(unique=True)
=======
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
class TodoUser(AbstractUser):
    email = models.EmailField(unique=True)
<<<<<<< HEAD
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'

=======
<<<<<<< HEAD

    def __str__(self):
        return f'{self.first_name} | {self.last_name}'
=======
>>>>>>> parent of b0be2de... Lesson_9_Done
>>>>>>> main
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
