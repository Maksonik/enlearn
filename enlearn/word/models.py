from django.db import models
from django.contrib.postgres.fields import ArrayField


class Word(models.Model):
    title = models.CharField(max_length=50)
    sound = models.FileField(blank=True)
    description = ArrayField(
        models.CharField(max_length=500)
    )

    class Meta:
        def __str__(self):
            return self.title

        ordering = [
            'title',
        ]
