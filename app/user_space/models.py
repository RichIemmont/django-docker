from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length = 200)
    race = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
