from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    CATEGORY = (
		('White & Cream', 'White & Cream'),
		('Pink', 'Pink'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Apricot & Orange', 'Apricot & Orange')
	) 

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Publication')
    photo = models.ImageField()
    

    def __str__(self):
	    return self.name


class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered')
	)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	products = models.CharField(null=True, max_length=700)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    
