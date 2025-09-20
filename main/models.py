import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [("a","A")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=101)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

#class Employee(models.Model):

#    name = models.CharField(max_length=255)
#    age = models.IntegerField()
#    persona = models.TextField()
#employee
# tiga field: name, age, persona
# nama: max 255 char
#age: integer
#persona: string
    
