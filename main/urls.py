from main.apps import MainConfig
from django.urls import path
from main.views import SectionList, SectionDetail, MaterialList, MaterialDetail, TestList, TestDetail, AnswerCreate


app_name = MainConfig.name

urlpatterns = [
    path('sections/', SectionList.as_view(), name='sections-list'),
    path('sections/<int:pk>/', SectionDetail.as_view(), name='section-detail'),
    path('materials/', MaterialList.as_view(), name='materials-list'),
    path('materials/<int:pk>/', MaterialDetail.as_view(), name='material-detail'),
    path('tests/', TestList.as_view(), name='tests-list'),
    path('tests/<int:pk>/', TestDetail.as_view(), name='test-detail'),
    path('tests/<int:pk>/answer/', AnswerCreate.as_view(), name='answer-create'),
]
