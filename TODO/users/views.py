from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import TodoUser
from .serializers import TodoUserModelSerializer


class TodoUserModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer
