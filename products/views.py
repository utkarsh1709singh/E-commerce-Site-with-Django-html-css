from django.shortcuts import render
from products.models import *
from accounts.models import *



# Create your views here.
def get_products(request,slug):
    
    try:
        products=product.objects.get(slug=slug)
        context={'product':products}
        if request.GET.get('size'):
            size=request.GET.get('size')
            price=product.get_products_prise_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
            print(price)
            
        return render(request, 'product/product.html' , context =context )
    
    except Exception as e:
        print(e)
        

    
        