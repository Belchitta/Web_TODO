from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.permissions import IsAdminUser, BasePermission
from .models import TodoUser
from .serializers import TodoUserModelSerializer, TodoUserModelSerializerV2


class TodoUserViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [BasePermission]
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1.2':
            return TodoUserModelSerializerV2
        return TodoUserModelSerializer


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
