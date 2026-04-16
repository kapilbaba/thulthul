from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    body_part = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
