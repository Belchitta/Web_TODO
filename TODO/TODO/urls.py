"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework.routers import DefaultRouter, SimpleRouter

from TodoLists.views import ToDoViewSet, ProjectViewSet
from users.views import TodoUserViewSet
from rest_framework.authtoken import views
<<<<<<< HEAD
=======

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )
=======
>>>>>>> main
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> parent of b0be2de... Lesson_9_Done
>>>>>>> main
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f

schema_view = get_schema_view(
    openapi.Info(
        title="Users",
        default_version="1.0",
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('users', TodoUserViewSet)
router.register('todos', ToDoViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
<<<<<<< HEAD
    path('api-auth-token/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
=======
<<<<<<< HEAD
    path('api-auth-token/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
=======
<<<<<<< HEAD
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
=======
    path('api-auth-token/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
>>>>>>> parent of b0be2de... Lesson_9_Done
>>>>>>> main
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
>>>>>>> 61f256aea00144b6b28399642f06426cd796928f
]
