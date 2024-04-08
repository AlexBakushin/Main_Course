from rest_framework import generics
from main.models import Section, Material, Test, Answer
from main.serliazers import SectionSerializer, MaterialSerializer, TestSerializer, AnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class SectionList(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer



class SectionDetail(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class MaterialList(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class TestList(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class AnswerCreate(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    fields = ['answer']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        serializer.save(test=test, user=self.request.user,
                        is_correct=test.correct_answer == serializer.validated_data['answer'])
