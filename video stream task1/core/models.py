from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


#video file db 
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    path = models.URLField()

    def __str__(self):
        return self.name
