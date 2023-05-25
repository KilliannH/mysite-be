from django.urls import include, path

from rest_framework import routers

from .views import QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)

urlpatterns = [
   path('', include(router.urls)),
]