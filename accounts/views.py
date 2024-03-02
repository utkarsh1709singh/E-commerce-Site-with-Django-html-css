from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.http import HttpResponseRedirect , HttpResponse
from .models import *
from products.models import *


def login_page(request):
   if request.method=='POST':
     
          
          email=request.POST.get('email')
          password=request.POST.get('password')
          
          user_obj=User.objects.filter(username=email)
          
          if not user_obj.exists():
            messages.warning(request, "User not found")
            return HttpResponseRedirect( request.path_info)
          
          if not user_obj[0].profile.is_email_verified:
             messages.warning(request, 'Email not verified')
             return HttpResponseRedirect( request.path_info)
        
          user_obj=authenticate(username=email,password=password)
          if user_obj:
              login(request ,user_obj)
              return redirect("/")
          
          messages.warning(request, "invalid Creditionals")
          return HttpResponseRedirect( request.path_info)
              
   return render(request, 'accounts/login.html')

def register_page(request):
      
    if request.method=='POST':
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          
          user_obj=User.objects.filter(username=email)
          
          if user_obj.exists():
            messages.warning(request, 'Email is already taken')
            return HttpResponseRedirect( request.path_info)
          
          user_obj=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
          )
          user_obj.set_password(password)
          user_obj.save()
          
          messages.success(request, 'Email has been sent to your mail')
          return HttpResponseRedirect( request.path_info)
          
          
    
          
          
    return render(request, "accounts/register.html")
  
  
def activate_email(request,email_token):
  try:
    user=profile.objects.get(email_token=email_token)
    user.is_email_verified=True
    user.save()
    return redirect('/')
  
  except Exception as e:
    return HttpResponse('invalid Email token')
  
def cart(request):
  context = {'cart' :Cart.objects.filter(is_paid =False ,user =request.user)}
  return render(request , 'accounts/cart.html',context)

def remove_cart(request,cart_item_uid):
  try:
      cart_item=CartItems.objects.get(uid= cart_item_uid)
      cart_item.delete()
  except Exception as e:
      print(e)   
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  
  

def add_to_cart(request ,uid):
    varient=request.GET.get('varient')
          
    Product=product.objects.get(uid=uid)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user = user , is_paid = False)
    
    cart_item = CartItems.objects.create(cart=cart ,Product=Product)
    if varient:
        varient=request.GET.get('varient')
        size_varient=SizeVarient.objects.get( size_name = varient )
        cart_item.size_varient=size_varient
        cart_item.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))