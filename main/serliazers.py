from rest_framework import serializers
from main.models import Section, Answer, Material, Test


class TestSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Test
    """
    class Meta:
        model = Test
        exclude = ['correct_answer']


class MaterialSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Material
    """
    test = TestSerializer(source='test_set', many=True, required=False)  # Добавляем поле test в сериализатор

    class Meta:
        model = Material
        fields = '__all__'

    def get_quantity_tests(self, instance):
        """
        Добавляет поле 'quantity_tests' с перечислением всех материалов данного раздела
        """
        return instance.test_set.all().count()


class SectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Section
    """
    material = MaterialSerializer(source='material_set', many=True, required=False)  # Добавляем поле material в сериализатор

    class Meta:
        model = Section
        fields = '__all__'

    def get_quantity_materials(self, instance):
        """
        Добавляет поле 'quantity_materials' с перечислением всех материалов данного раздела
        """
        return instance.material_set.all().count()


class AnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Answer
    """
    class Meta:
        model = Answer
        fields = '__all__'
