from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import School, ClassGroup, Student, Test, Question, AnswerOption, StudentAnswer
from .serializers import SchoolSerializer, ClassGroupSerializer, StudentSerializer, TestSerializer, QuestionSerializer, AnswerOptionSerializer, StudentAnswerSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ClassGroupViewSet(viewsets.ModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    # Проверка наличия теста по ID
    def retrieve(self, request, *args, **kwargs):
        test_id = kwargs.get('pk')
        test = self.queryset.filter(test_id=test_id).first()
        if not test:
            return Response({"error": "Тест с таким ID не найден"}, status=404)
        serializer = self.get_serializer(test)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerOptionViewSet(viewsets.ModelViewSet):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer

class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

def home(request):
    return render(request,'index.html')