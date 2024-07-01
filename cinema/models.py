from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"Movie: {self.title}"