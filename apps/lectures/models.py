from django.db import models

from apps.utils.models import Timestamps

class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    slides_url = models.CharField(max_length=255)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    notes = models.TextField()


