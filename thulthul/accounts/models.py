from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GOAL_CHOICES = [
        ('fat_loss', 'Fat Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintain', 'Maintain'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
