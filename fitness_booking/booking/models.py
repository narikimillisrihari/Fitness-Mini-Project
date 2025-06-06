from django.db import models
from django.utils import timezone
# Create your models here.

class Fitness(models.Model):
    name=models.CharField(max_length=250)
    instructor=models.CharField(max_length=250)
    date_time = models.DateTimeField()
    available_slots=models.IntegerField()

    def __str__(self):
        return self.instructor
class Book(models.Model):
    fitness_class=models.ForeignKey(Fitness,on_delete=models.CASCADE)
    client_name=models.CharField(max_length=250)
    client_email=models.EmailField()

    def __str__(self):
        return self.client_name
    
        