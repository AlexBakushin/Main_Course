from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from users.models import User


class UserTestCase(APITestCase):
    def test_create_user(self):
        """
        Тест на создание пользователя
        """
        self.client = APIClient()

        data = {
            'email': 'test1@test.test',
            'password': '12345',
            'first_name': 'test1',
            'last_name': 'test1',
        }

        response = self.client.post('/users/user/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_user(self):
        """
        Тест на получение списка пользователей
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test2@test.test", first_name="test2", last_name="test2", is_superuser=False, is_staff=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/users/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        """
        Тест на получение пользователя
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test3@test.test", first_name="test3", last_name="test3", is_superuser=False, is_staff=False)
        self.client.force_authenticate(user=self.user)

        User.objects.create(
            email="test4@test.test",
            is_superuser=False,
            is_staff=False,
            first_name="test4",
            last_name="test4",
        )

        response = self.client.get('/users/user/10/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        """
        Тест на обновление пользователя
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test5@test.test", first_name="test5", last_name="test5", is_superuser=False, is_staff=False)
        self.client.force_authenticate(user=self.user)

        data = {
            'email': 'test6@test.test',
            'password': '12345',
            'first_name': 'test6',
            'last_name': 'test6',
        }

        response = self.client.put('/users/user/13/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        """
        Тест на удаление пользователя
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test7@test.test", first_name="test7", last_name="test7", is_superuser=False, is_staff=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.delete('/users/user/9/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
