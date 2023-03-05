from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Toy(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.color} {self.name}"
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs = {"pk": self.id})


# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    true_finch = models.BooleanField()
    description = models.TextField(max_length=250)
    length = models.IntegerField()
    wingspan = models.IntegerField()
    picture = models.CharField(max_length=500)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {"finch_id": self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default = MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        #This method is coming from django
        # produced like this: get_<name_of_field>_display()
        return f"{self.get_meal_display()} on {self.date}"
    
    # Change default sort
    class Meta:
        ordering = ['-date']