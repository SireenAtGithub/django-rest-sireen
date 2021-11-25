from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    score = models.IntegerField()

    def __str__(self):
        return self.first_name

# Create your models here.


# Create your models here.
