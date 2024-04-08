from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from main.models import Material, Section, Test, Answer


class SectionTestCase(APITestCase):
    def test_list_section(self):
        """
        Тест на получение списка разделов
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test10@test.test", first_name="test10", last_name="test10",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/sections/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_material(self):
        """
        Тест на получение списка материалов
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test11@test.test", first_name="test11", last_name="test11",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/materials/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_test(self):
        """
        Тест на получение списка тестов
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test12@test.test", first_name="test12", last_name="test12",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/tests/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_section(self):
        """
        Тест на получение раздела
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test13@test.test", first_name="test13", last_name="test13",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        Section.objects.create(
            title="test1",
            description="test1"
        )

        response = self.client.get('/sections/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_material(self):
        """
        Тест на получение материала
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test14@test.test", first_name="test14", last_name="test14",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        Material.objects.create(
            title="test1",
            content="test1",
            section=Section.objects.create(title="test2", description="test2")
        )

        response = self.client.get('/materials/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_test(self):
        """
        Тест на получение теста
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test15@test.test", first_name="test15", last_name="test15",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        Test.objects.create(
            material=Material.objects.create(title="test1", content="test1",
                                             section=Section.objects.create(title="test2", description="test2")),
            question="test1",
            correct_answer="test1"
        )

        response = self.client.get('/tests/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_answer_create(self):
        """
        Тест на создание ответа
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test15@test.test", first_name="test15", last_name="test15",
                                        is_superuser=False,
                                        is_staff=False)
        self.client.force_authenticate(user=self.user)

        Test.objects.create(
            material=Material.objects.create(title="test1", content="test1",
                                             section=Section.objects.create(title="test2", description="test2")),
            question="test1",
            correct_answer="test1"
        )

        data = {
            'answer': 'test1'
        }

        response = self.client.post('/tests/1/answer/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
