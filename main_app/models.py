from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    true_finch = models.BooleanField()
    description = models.TextField(max_length=250)
    length = models.IntegerField()
    wingspan = models.IntegerField()
    picture = models.CharField(max_length=500)

    def __str__(self):
        return self.name
