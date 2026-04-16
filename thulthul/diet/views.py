from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from accounts.models import UserProfile

class DietGenerateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        goal = user_profile.goal
        if not goal:
            return Response({"error": "Please set your goal first."}, status=status.HTTP_400_BAD_REQUEST)

        if goal == 'fat_loss':
            diet = {
                "breakfast": "Oatmeal with berries and a scoop of protein powder",
                "lunch": "Grilled chicken salad with mixed greens and vinaigrette",
                "dinner": "Baked salmon with quinoa and steamed broccoli"
            }
        elif goal == 'muscle_gain':
            diet = {
                "breakfast": "Eggs, whole grain toast, and avocado",
                "lunch": "Turkey sandwich with sweet potato and Greek yogurt",
                "dinner": "Beef stir-fry with rice and vegetables"
            }
        else:  # maintain
            diet = {
                "breakfast": "Greek yogurt with nuts and fruit",
                "lunch": "Tuna wrap with salad",
                "dinner": "Grilled fish with couscous and salad"
            }

        return Response({"goal": goal, "diet_plan": diet})
