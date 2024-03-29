from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
import  datetime
# from django.utils.timezone import now

# dat=now()
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50,blank = True,null=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return(self.name)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price  = models.IntegerField(default=0)
    description = models.CharField(max_length=200,default='',blank=True)
    image =models.ImageField(upload_to="product/")
    category = models.ForeignKey(Category, on_delete=CASCADE)
    multiple_images = models.TextField(max_length=255)
    offer =  models.BooleanField(default = False)
    offer_price = models.IntegerField(default = 0)


    @staticmethod
    def get_all_products():
        return Product.objects.all().order_by('id')

    @staticmethod
    def get_products_by_category_id(category_id):
        return Product.objects.filter(category_id = category_id)

    # def __str__(self):
    #     return(self.name)

class AddCarousel(models.Model):
  
    name = models.TextField(max_length=255)

  

    def __str__(self):
        return(self.name)

class Pincode(models.Model):
    zipcode = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=255)

    # def __str__(self):
    #     return (self.user)
     



class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address  =models.CharField(max_length=255,default='',blank=True)
    phone = models.CharField(max_length=15,default='',blank=True)
    order_dated = models.DateField(default = datetime.datetime.today)
 

class Comments(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    date_added  =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.product.name)

class Rating(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    date_added  =models.DateTimeField(auto_now_add=True)
    choice = models.IntegerField()

    def __str__(self):
        return (self.product.name)

class Coupon(models.Model):
    coupon = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    count = models.IntegerField(default = 0)
    offer =  models.BooleanField(default = False)
    start_time = models.DateField(null = True,blank = True)
    end_time = models.DateField(null = True, blank = True)



    # def __str__(self):
    #     return(self.coupon)


    