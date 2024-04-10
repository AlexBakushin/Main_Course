from rest_framework import generics
from main.models import Section, Material, Test, Answer
from main.serliazers import SectionSerializer, MaterialSerializer, TestSerializer, AnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from main.paginators import BasePaginator


class SectionCreate(generics.CreateAPIView):
    """
    API endpoint создания раздела
    """
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]


class SectionList(generics.ListAPIView):
    """
    API endpoint списка разделов
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    pagination_class = BasePaginator
    permission_classes = [IsAuthenticated]


class SectionDetail(generics.RetrieveAPIView):
    """
    API endpoint детального просмотра раздела
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]


class MaterialCreate(generics.CreateAPIView):
    """
    API endpoint создания материала
    """
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]


class MaterialList(generics.ListAPIView):
    """
    API endpoint списка материалов
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    pagination_class = BasePaginator
    permission_classes = [IsAuthenticated]


class MaterialDetail(generics.RetrieveAPIView):
    """
    API endpoint детального просмотра материала
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]


class TestCreate(generics.CreateAPIView):
    """
    API endpoint создания теста
    """
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]


class TestList(generics.ListAPIView):
    """
    API endpoint списка тестов
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = BasePaginator
    permission_classes = [IsAuthenticated]


class TestDetail(generics.RetrieveAPIView):
    """
    API endpoint детального просмотра теста
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]


class AnswerCreate(generics.CreateAPIView):
    """
    API endpoint создания ответа
    """
    serializer_class = AnswerSerializer
    fields = ['answer']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Добавляет ответ пользователя к тесту
        :param serializer:
        :return:
        """
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        serializer.save(test=test, user=self.request.user,
                        is_correct=test.correct_answer == serializer.validated_data['answer'])
