from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import TodoUser
from .serializers import TodoUserModelSerializer


class TodoUserViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = TodoUserModelSerializer
    queryset = TodoUser.objects.all()
