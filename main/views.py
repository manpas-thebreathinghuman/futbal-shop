import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ShopForm#, CarForm
from main.models import Product#, Car, Employee
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

@login_required(login_url='/login')
def show_main(request):
    #pembuatan yg di template
    if not User.objects.filter(username="Budi_bedagang").exists():
        budi = User.objects.create_user(username="Budi_bedagang", password="bedagangbukanbegadang")

        Product.objects.create(user=budi, name='Football', price=100000, description="Buat diliatin jadi nonton bola. HD quality", thumbnail="https://images.rawpixel.com/image_social_square/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvam9iNjg0LTI0NS12LmpwZw.jpg", category="spourts item", is_featured=False)
        Product.objects.create(user=budi, name="Special custom banner", price=500000, description="Custom banner so special it will make your sunday marvelous",thumbnail="https://static.vecteezy.com/system/resources/thumbnails/000/701/690/small_2x/abstract-polygonal-banner-background.jpg", category="others", is_featured=False)
        Product.objects.create(user=budi, name="T-shirt putih", price=80000, description="Baju putih buat main bola. Tapi hati-hati jangan kotor soalnya bajunya putih", thumbnail="https://png.pngtree.com/png-clipart/20230206/ourmid/pngtree-realistic-white-t-shirt-vector-for-mockup-png-image_6584050.png", category="cloathing item", is_featured=False)

    if not User.objects.filter(username="Minoru").exists():
        minoru = User.objects.create_user(username="Minoru", password="GutsTraining")

        Product.objects.create(user=minoru, name='Sprinting Shoe', price=1000, description="The hottest new shoe from a popular sprinting brand from another universe",thumbnail="https://gametora.com/images/umamusume/items/item_icon_00001.png", category="futwear", is_featured=False)
        Product.objects.create(user=minoru, name="Dirt-resistant shoe", price=1000, description="Brand-name shoe that cleans the sloppiest of dirst. From another universe",thumbnail="https://gametora.com/images/umamusume/items/item_icon_00013.png", category="futwear", is_featured=False)
        Product.objects.create(user=minoru, name="Alarm clock", price=2000, description="magic alarm clock from another universe that resets your bad day",thumbnail="https://img.game8.co/4225281/7aec4998c56fe28a363b409f6a11ab25.png/show", category="merchant dice", is_featured=False)

    filter_type = request.GET.get("filter", "all") #default 'all'

    if filter_type == "all":
        item_list = Product.objects.all()
        print(item_list)
    else:
        item_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406411830',
        'name': request.user.username,
        'class': 'PBP E',
        'item_list': item_list,
        'categories': Product.CATEGORY_CHOICES,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

#bisa kyk gini juga:

#def new_employee(request):

#    employee = Employee.objects.create(name = "Danniel", age = 20, persona = "baik banget buat challenge")
#    context = {
#        'name': employee.name,
#        'age': employee.age,
#        'persona': employee.persona

#    }
#    return render(request, "employeee.html", context)

def new_item(request):
    form = ShopForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit = False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "new_item.html", context)

#def new_car(request):
    #form = CarForm(request.POST or None)

    #if form.is_valid() and request.method == "POST":
        #item_entry = form.save(commit = False)
        #item_entry.user = request.user
        #item_entry.save()
        #return redirect('main:show_main')
    
    #context = {'form': form}
    #return render(request, "new_car.html", context)

def edit_item(request, id):
    item = get_object_or_404(Product, pk=id)
    form = ShopForm(request.POST or None, instance=item)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_item.html", context)

def delete_item(request, id):
    news = get_object_or_404(Product, pk=id)
    news.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yur ackount has been successfuly created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
