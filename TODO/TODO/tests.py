import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

import users
from users.views import TodoUserViewSet
from TodoLists.views import ProjectViewSet, ToDoViewSet
from users.models import TodoUser
from TodoLists.models import Project, ToDo


class TestTODOModelViewSet(TestCase):
    # APIRequestFactory. Неавторизованный пользователь не должен иметь доступа.
    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin123'
        self.email = 'admin@gmail.com'
        self.data = {'username': 'IvanDorn',
                     'first_name': 'Ivan',
                     'last_name': 'Dorn',
                     'email': 'test@email.com'}
        self.data_put = {'username': 'IvanDorn',
                         'first_name': 'Иван',
                         'last_name': 'Дорн',
                         'email': 'test@email.com'}
        self.url = 'api/users/'
        self.admin = TodoUser.objects.create_superuser(username=self.name,
                                                       password=self.password,
                                                       email=self.email)

    def test_get_list_unauthorized(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = TodoUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # APIRequestFactory. Проверка доступности данных авторизированному пользователю.
    def test_get_list(self):
        factory = APIRequestFactory()
        admin = self.admin
        request = factory.get(self.url)
        force_authenticate(request, admin)
        view = TodoUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestServiceUserModel(TestCase):
    # APIClient. Тест редактирования, используя права администратора.
    def test_edit(self):
        user = mixer.blend(TodoUser)
        client = APIClient()
        admin = TodoUser.objects.create_superuser(username='admin',
                                                  password='admin123',
                                                  email='admin@gmail.com')
        client.login(username='admin', password='admin123')
        response = client.put(f'/api/users/{user.id}/', {'id': '1',
                                                         'username': 'IvanDorn',
                                                         'first_name': 'Иван',
                                                         'last_name': 'Дорн',
                                                         'email': 'test@email.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestNumPy(APISimpleTestCase):
    # APISimpleTestCase. Тест работы библиотеки Numpy.
    def test_sin(self):
        import numpy as np
        self.assertEqual(np.sin(np.pi / 2.), 1.0)


class TestToDoAdd(APITestCase):
    # APITestCase. Тест добавления новой задачи.
    def test_add_todo_to_project(self):
        project = mixer.blend(Project)
        user = mixer.blend(TodoUser)
        todo = mixer.blend(ToDo)
        admin = TodoUser.objects.create_superuser(username='admin',
                                                  password='admin123',
                                                  email='admin@gmail.com')
        self.client.login(username='admin', password='admin123')
        response = self.client.put(f'/api/todos/{todo.id}/',
                                   {'id': '11', 'project': project.id,
                                    'text': 'SampleText', 'creator': user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
