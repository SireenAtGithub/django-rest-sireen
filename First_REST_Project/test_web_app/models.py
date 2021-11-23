from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    song_name = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
