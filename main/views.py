from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ShopForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    items_list = Product.objects.all()

    context = {
        'npm': '2406411830',
        'name': 'Muhammad Fadhlurrohman Pasya',
        'class': 'PBP E',
        'item_list': items_list
    }

    return render(request, "main.html", context)

def new_item(request):
    form = ShopForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "new_item.html", context)

def show_item(request, id):
    item = get_object_or_404(Product, pk=id)
    
    context = {
        'item': item
    }

    return render(request, "item_detail.html", context)

def show_xml(request):
     item_list = Product.objects.all()
     xml_data = serializers.serialize("xml", item_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    item_list = Product.objects.all()
    json_data = serializers.serialize("json", item_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, item_id):
    try:
        item_thing = Product.objects.filter(pk=item_id) # Harusnya news_item tapi diganti jadi item_thing. Masa item_item?
        xml_data = serializers.serialize("xml", item_thing)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, item_id):
    try:
        item_thing = Product.objects.get(pk=item_id)
        json_data = serializers.serialize("json", [item_thing])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

# Create your views here.
