from django.urls import path
from .views import ExerciseListView, WorkoutGenerateView

urlpatterns = [
    path('exercises/', ExerciseListView.as_view(), name='exercises'),
    path('generate/', WorkoutGenerateView.as_view(), name='workout_generate'),
]