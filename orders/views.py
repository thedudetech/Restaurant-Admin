from django.shortcuts import render
from products.models import Products
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from .models import GetOrder
# import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def TakeAway(request):
    Productlist = Products.objects.all()

    product_data = {
    "product_data": Productlist
    }

    return render(request, 'take-away.html',product_data)

def getPrice(request,id):
    #product_name = Products.objects.values_list('product_name',flat=True).get(id=id)
    product_price = Products.objects.values_list('product_price',flat=True).get(id=id)
    # print(product_name)
    # print(product_price)
    # price_serialized = serializers.serialize('json', product_price)

    # data = json.dumps({ 'data' : product_price })
    # return JsonResponse(price_serialized)
    return HttpResponse(json.dumps(product_price), content_type='application/json')

def getOrder(request):
    if request.method == 'POST':
        kotid = 0
        
        item_name =  request.POST['item']
        note =  request.POST['note']
        qnty =  request.POST['qntyno']
        price =  request.POST['amount']
        
        savekot = GetOrder(kotid=0,item_name=item_name,note=note,qnty=qnty,price=price)
        savekot.save()
        message = 'update successful'
    return HttpResponse(message)
