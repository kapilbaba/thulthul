from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Exercise
from .serializers import ExerciseSerializer
from accounts.models import UserProfile
import random

class ExerciseListView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAuthenticated,)

class WorkoutGenerateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        goal = user_profile.goal
        if not goal:
            return Response({"error": "Please set your goal first."}, status=status.HTTP_400_BAD_REQUEST)

        exercises = list(Exercise.objects.all())
        if len(exercises) < 5:
            return Response({"error": "Not enough exercises in database."}, status=status.HTTP_400_BAD_REQUEST)

        selected_exercises = random.sample(exercises, 5)

        workout = []
        for ex in selected_exercises:
            if goal == 'fat_loss':
                sets = 3
                reps = '12-15'
            elif goal == 'muscle_gain':
                sets = 4
                reps = '8-12'
            else:  # maintain
                sets = 3
                reps = '10-12'
            workout.append({
                'exercise': ex.name,
                'sets': sets,
                'reps': reps,
                'body_part': ex.body_part,
                'description': ex.description
            })

        return Response({"goal": goal, "workout": workout})
