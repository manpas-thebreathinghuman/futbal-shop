from django.forms import ModelForm
from main.models import Product#, Car

class ShopForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]

#class CarForm(ModelForm):
    #class Meta:
        #model = Car
        #fields = ["name", "brand", "stock"]
