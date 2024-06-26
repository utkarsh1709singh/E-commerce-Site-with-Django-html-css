from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class category(BaseModel):
    category_name= models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image =models.ImageField(upload_to="category")
    
    def save(self ,*args ,**kwargs):
        self.slug=slugify(self.category_name)
        super(category,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.category_name

class ColorVarient(BaseModel):
    color_name= models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.color_name
    
class SizeVarient(BaseModel):
    size_name=models.CharField(max_length=100) 
    price=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size_name

class product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name="products")
    price=models.IntegerField()
    product_discription=models.TextField()
    color_varient=models.ManyToManyField(ColorVarient ,blank=True)
    size_varient=models.ManyToManyField(SizeVarient, blank=True)
    
    
    def save(self ,*args ,**kwargs):
        self.slug=slugify(self.product_name)
        super(product,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.product_name
    
    def get_products_prise_by_size(self,size):
        return self.price + SizeVarient.objects.get(size_name=size).price
        

    
class ProductImage(BaseModel):
    product=models.ForeignKey(product,on_delete=models.CASCADE,related_name="product_images")
    image=models.ImageField(upload_to="product")
      