from django.shortcuts import render
from .models import Products, Product_Category, Product_Additionals
from . import table
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from .serializers import ProductsSerializers, ProductsCatSerializers
# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_product(request):
    if request.method == 'POST':
        print("Inside Register Post")
        product_photo = request.POST['product_photo']
        
        food_region = request.POST['food_region']
        product_name = request.POST['product_name']
        product_details = request.POST['product_details']
        additionals = request.POST.getlist('additonals')
        product_quantity = request.POST['product_quantity']
        product_price = request.POST['product_price']
        
        print(additionals)
        b = Products(product_photo=product_photo,food_region=food_region, product_name=product_name, product_details=product_details, additionals=additionals, product_quantity=product_quantity, product_price=product_price)
        b.save()
    pro_cat = Product_Category.objects.all()
    additionals = Product_Additionals.objects.all()
    return render(request, 'restaurant-upload-menu.html', {'pro_cat':pro_cat,'additionals': additionals})


def view_product(request):
    
    product = table.ProductTable()
    
    return render(request, 'view_menu.html', {'product': product })

product_ID = None
def update_product(request):
    pro_cat = Product_Category.objects.all()
    additionals = Product_Additionals.objects.all()
    if request.method == 'POST':
            
        print("Inside Update Post")
        if 'btn_search' in request.POST:
            print("In Button Search")
            global product_ID
            product_ID = request.POST['pid']
            
            print(product_ID)
            ckpid = Products.objects.filter(id=product_ID)
            if ckpid:
                
                
                food_region = Products.objects.values_list('food_region',flat=True).get(id=product_ID)
                product_name = Products.objects.values_list('product_name',flat=True).get(id=product_ID)
                product_details = Products.objects.values_list('product_details',flat=True).get(id=product_ID)
                product_quantity = Products.objects.values_list('product_quantity',flat=True).get(id=product_ID)
                product_price = Products.objects.values_list('product_price',flat=True).get(id=product_ID)
                
                return render(request, 'update-menu.html', {'food_region':food_region,'product_name' : product_name,'product_details' :product_details,'product_quantity':product_quantity,'product_price':product_price,'pro_cat':pro_cat,'additionals': additionals})
        elif 'btn_update' in request.POST:
            print("In Button Update")
            
            print("Product ID in UPdate Post",product_ID)
            food_region = request.POST['food_region']
            product_name = request.POST['product_name']
            product_details = request.POST['product_details']
            additionals = request.POST.getlist('additonals')
            product_quantity = request.POST['product_quantity']
            product_price = request.POST['product_price']
            
            Products.objects.filter(id=product_ID).update(food_region=food_region,product_name=product_name,product_details=product_details, additionals=additionals,product_quantity=product_quantity,product_price=product_price)
            
            
    
    return render(request, 'update-menu.html', {'pro_cat':pro_cat,'additionals': additionals})
    


def delete_menu(request):
    
    if request.method == 'POST':
            
        print("Inside Update Post")
        if 'btn_search' in request.POST:
            print("In Button Search")
            global product_ID
            product_ID = request.POST['pid']
            
            print(product_ID)
            ckpid = Products.objects.filter(id=product_ID)
            if ckpid:
                
                
                
                food_region = Products.objects.values_list('food_region',flat=True).get(id=product_ID)
                product_name = Products.objects.values_list('product_name',flat=True).get(id=product_ID)
                product_details = Products.objects.values_list('product_details',flat=True).get(id=product_ID)
                product_quantity = Products.objects.values_list('product_quantity',flat=True).get(id=product_ID)
                product_price = Products.objects.values_list('product_price',flat=True).get(id=product_ID)
                
                return render(request, 'delete-menu.html', {'food_region':food_region,'product_name' : product_name,'product_details' :product_details,'product_quantity':product_quantity,'product_price':product_price,})
        elif 'btn_delete' in request.POST:
            print("In Button Delete")
            
            print("Product ID in Delete Post",product_ID)
           
            
            Products.objects.filter(id=product_ID).delete()
            
            
    
    return render(request, 'delete-menu.html')

def menus_one(request):

    Productlist = Products.objects.all()

    product_data = {
    "product_data": Productlist
    }


    return render(request, 'restaurant-menu-one.html',product_data)

def menus_two(request):

    Productlist = Products.objects.all()

    product_data = {
    "product_data": Productlist
    }


    return render(request, 'restaurant-menu-two.html',product_data)

def menus_three(request):

    Productlist = Products.objects.all()

    product_data = {
    "product_data": Productlist
    }


    return render(request, 'restaurant-menu-three.html',product_data)

# products/
class Productlist(APIView):
    # def get(self, request):
    #     products = Products.objects.all()
    #     serializer = ProductsSerializers(products, many=True)
    #     return Response(serializer.data)
    def post(self, request):
        products = Products.objects.filter(food_region=1)
        serializer = ProductsSerializers(products, many=True)
        return Response(serializer.data)

# procat/
class ProductCategory(APIView):
    # def get(self, request):
    #     procats = Product_Category.objects.all()
    #     for i in procats:
    #         products = Products.objects.filter(food_region=i.id)
    #         print(i)

    #     serializer = ProductsCatSerializers(products, many=True)
    #     return Response(serializer.data)
    def post(self, request):
        procats = Product_Category.objects.all()
        for i in procats:
            products = Products.objects.filter(food_region=i.id)
            print(i)

        serializer = ProductsCatSerializers(products, many=True)
        return Response(serializer.data)
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render(request, 'page-login.html')

