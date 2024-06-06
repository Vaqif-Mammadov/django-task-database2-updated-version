from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthplace = models.TextField()
    residence = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    university = models.TextField()
    specialty = models.CharField(max_length=100)  # Bu sahəni əlavə edin
    hobbies = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
