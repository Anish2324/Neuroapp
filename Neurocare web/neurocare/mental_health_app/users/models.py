from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    stress_level = models.FloatField(default=0.0)
    anxiety_level = models.FloatField(default=0.0)
    depression_level = models.FloatField(default=0.0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    

