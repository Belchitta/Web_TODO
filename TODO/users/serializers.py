from rest_framework.serializers import ModelSerializer
from .models import TodoUser


class TodoUserModelSerializer(ModelSerializer):
    class Meta:
        model = TodoUser
<<<<<<< HEAD
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'


class TodoUserModelSerializerV2(ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')
=======
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
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
