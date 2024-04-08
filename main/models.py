from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Section(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Material(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Раздел')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Test(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    correct_answer = models.CharField(max_length=255, verbose_name='Правильный ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест', **NULLABLE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    answer = models.CharField(max_length=255, verbose_name='Ответ')
    is_correct = models.BooleanField(verbose_name='Правильность', **NULLABLE)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ на тест'
        verbose_name_plural = 'Ответы на тесты'
