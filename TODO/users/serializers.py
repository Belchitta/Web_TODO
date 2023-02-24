from rest_framework.serializers import ModelSerializer
from .models import TodoUser


class TodoUserModelSerializer(ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('user_name', 'first_name', 'last_name', 'email', 'birthday_year')
