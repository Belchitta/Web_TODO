from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.permissions import IsAdminUser, BasePermission
from .models import TodoUser
from .serializers import TodoUserModelSerializer


class TodoUserViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = TodoUserModelSerializer
    queryset = TodoUser.objects.all()


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
