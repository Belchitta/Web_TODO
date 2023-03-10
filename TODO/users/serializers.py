from rest_framework.serializers import ModelSerializer
from .models import TodoUser


class TodoUserModelSerializer(ModelSerializer):
    class Meta:
        model = TodoUser
<<<<<<< HEAD
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'
=======
<<<<<<< HEAD
        fields = ('user_name', 'first_name', 'last_name', 'email', 'birthday_year')
=======
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'
>>>>>>> parent of b0be2de... Lesson_9_Done
>>>>>>> main
