from django.urls import path
from .views import DietGenerateView

urlpatterns = [
    path('generate/', DietGenerateView.as_view(), name='diet_generate'),
]