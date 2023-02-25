from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.viewsets import ModelViewSet

from .models import TodoUser
from .serializers import TodoUserModelSerializer


class TodoUserModelViewSet(ModelViewSet):
    renderer_classes = [AdminRenderer]
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer
