from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Test, StudentAnswer
from .serializers import TestSerializer

# ViewSet для управления тестами
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    # Эндпоинт для отправки ответов студентов
    @action(detail=True, methods=['post'])
    def submit_answer(self, request, pk=None):
        test = self.get_object()
        student = request.data.get('student')
        answers = request.data.get('answers')

        for ans in answers:
            StudentAnswer.objects.create(
                student_id=student,
                test=test,
                question_id=ans['question_id'],
                answer_id=ans['answer_id']
            )
        return Response({'status': 'answers submitted'}, status=status.HTTP_200_OK)

    # Эндпоинт для получения теста по ID
    @action(detail=False, methods=['get'])
    def test_by_id(self, request):
        test_id = request.query_params.get('test_id')
        test = Test.objects.filter(id=test_id).first()
        if not test:
            return Response({'error': 'Invalid test ID'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(test)
        return Response(serializer.data)

def home(request):
    return render(request, 'index.html')