from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    stress_level = models.FloatField(default=0.0)
    anxiety_level = models.FloatField(default=0.0)
    depression_level = models.FloatField(default=0.0)
