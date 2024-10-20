# tests/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test
from .serializers import TestSerializer

class TestDetailView(APIView):
    def get(self, request, test_id):
        try:
            test = Test.objects.get(test_id=test_id)
            serializer = TestSerializer(test)
            return Response(serializer.data)
        except Test.DoesNotExist:
            return Response({'error': 'Test not found'}, status=status.HTTP_404_NOT_FOUND)

def home(request):
    return render(request, 'index.html')