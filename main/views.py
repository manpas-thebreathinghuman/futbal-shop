from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Shoe',
        'price': 'Rp999.999',
        'description' : 'the best shoe in the industree'
    }

    return render(request, "main.html", context)
# Create your views here.
