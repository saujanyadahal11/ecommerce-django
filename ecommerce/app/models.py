from distutils.command.upload import upload
from itertools import product
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
ZONECHOICES=(
                ('Mechi','Mechi'),('Koshi','Koshi'), ('Sagarmatha','Sagarmatha'), ('Janakpur','Janakpur'),
                ('Bagmati','Bagmati'), ('Narayani','Narayani'),('Gandaki','Gandaki'),
                ('Dhaulagiri','Dhaulagiri'),('Lumbini','Lumbini'), ('Karnali','Karnali'), 
                ('Rapti','Rapti'), ('Bheri','Bheri'), ('Seti','Seti'), ('Mahakali','Mahakali'),
)
GENDERCHOICES=(
                ('M','Male'),('F','Female'),
)
class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    zone=models.CharField(choices=ZONECHOICES, max_length=50)

def _str_(self):
    return str(self.id)

class Categories(models.Model):
    category=models.CharField(max_length=20)
    
def _str_(self):
    return str(self.id)

class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField()
    discount=models.FloatField()
    description=models.TextField()
    specification=models.TextField()
    brand=models.CharField(max_length=20)
    category=models.CharField(max_length=40)
    gender=models.CharField(choices=GENDERCHOICES, max_length=10)
    product_img=models.ImageField(upload_to='productimg')
    status=models.CharField(max_length=20)
    
def _str_(self):
    return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

def _str_(self):
    return str(self.id)

STATUS_CHOICES=(
    ('Pending','Pending'), ('Accepted','Accepted'), ('Cancel','Cancel'), 
    ('Packed','Packed'), ('Shipping','Shipping'), ('Delivered','Delivered'), 
)

class OrderedPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    orderedDate=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')


