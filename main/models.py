import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [("futwear","Futwear"),
                        ("cloathing itm","Cloathing itm"),
                        ("merchant dice","Merchant dice"),
                        ("spourts itm", "Spourts itm"),
                        ("others","Others")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=101)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='others')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#class Employee(models.Model):

#    name = models.CharField(max_length=255)
#    age = models.IntegerField()
#    persona = models.TextField()
#employee
# tiga field: name, age, persona
# nama: max 255 char
#age: integer
#persona: string
    
#class Car(models.Model):
    #name = models.CharField(max_length=255)
    #brand = models.CharField(max_length=255)
    #stock = models.IntegerField()

    #def __str__(self):
        #return self.name
    #bikin model namanya car/mobil
    # atribute Name (255 char) Brand (255 char) Stock (int)
