from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=200, blank=True)
    profession = models.CharField(max_length=200, blank=True)
    education = models.CharField(max_length=200, blank=True)
    religion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} ({self.city})"
