from __future__ import unicode_literals
from django.db import models

class Cafe(models.Model):
    cafe_name = models.CharField(max_length=20)
    cafe_color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cafe_name
        
class Coffee(models.Model):
    coffee_name = models.CharField(max_length=50)
    coffee_price = models.IntegerField(default=0)
    coffee_status = models.BooleanField(default=False)
    cafe = models.ForeignKey(Cafe) 
    
    def __str__(self):
        return self.coffee_name

# Create your models here.
