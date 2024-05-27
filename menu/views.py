from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizzas

# / menu
def index(request):
    # pizzas = Pizzas.objects.all()
    # pizzas_names_and_prices = [pizza.nom + " : " + str(pizza.prix) + "$" for pizza in pizzas]
    # pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)
    # return HttpResponse("Les pizzas " + pizzas_names_and_prices_str)
    pizzas = Pizzas.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas' : pizzas})


def api_get_pizzas(request):
    pizzas = Pizzas.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)