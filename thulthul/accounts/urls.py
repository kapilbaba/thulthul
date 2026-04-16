from django.urls import path
from .views import RegisterView, LoginView, ProfileView, GoalView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('goal/', GoalView.as_view(), name='goal'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]