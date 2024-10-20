# tests/models.py
from django.db import models

class Test(models.Model):
    test_id = models.CharField(max_length=6, unique=True)  # Уникальный ID теста (6 цифр)
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    class_name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    duration = models.IntegerField(default=60)  # Продолжительность теста в минутах

    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
