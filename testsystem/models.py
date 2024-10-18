from django.db import models
from django.utils import timezone

# Модель для школы
class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель для класса
class ClassGroup(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.school.name}"

# Модель для учеников
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель для теста
class Test(models.Model):
    title = models.CharField(max_length=100)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.DurationField(default=timezone.timedelta(hours=1))
    test_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

# Модель для вопроса
class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text

# Модель для вариантов ответа (включает правильный ответ)
class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.JSONField()  # Список вариантов

    def __str__(self):
        return f"Вопрос: {self.question.text}, Варианты: {self.options}"

# Модель для ответов учеников
class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def check_answer(self):
        self.is_correct = self.selected_answer == self.question.correct_answer
        self.save()

    def __str__(self):
        return f"Ответ от {self.student.first_name} на вопрос {self.question.text}"
