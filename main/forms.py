from django.forms import ModelForm
from main.models import Product

class ShopForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]