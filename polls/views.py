from rest_framework import viewsets, permissions
# provide the advantage of combining multiple sets of logic into a single class.

from .serializers import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice


class QuestionViewSet(viewsets.ModelViewSet):
   queryset = Question.objects.all()
   serializer_class = QuestionSerializer
   permission_classes = [permissions.IsAuthenticated]


class ChoiceViewSet(viewsets.ModelViewSet):
   queryset = Choice.objects.all()
   serializer_class = ChoiceSerializer
   permission_classes = [permissions.IsAuthenticated]