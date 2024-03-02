from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(category)

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price']
    inlines=[ProductImageAdmin]

@admin.register(ColorVarient)
class ColorVarientAdmin(admin.ModelAdmin):
    list_display=['color_name', 'price']
    model= ColorVarient
           
@admin.register(SizeVarient)   
class SizeVarientAdmin(admin.ModelAdmin):
    list_display=['size_name', 'price']
    model= SizeVarient 
    
admin.site.register(product,ProductAdmin)

admin.site.register(ProductImage)
