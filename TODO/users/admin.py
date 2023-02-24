from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import TodoUser


@admin.register(TodoUser)
class BookAdmin(ModelAdmin):
    pass
