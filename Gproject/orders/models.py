from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE, 'Live'), (DELETE, 'Delete'))
    cart_stage=1
    order_confirmed=1
    order_processed=2
    order_delivered=3
    order_rejected=4
    status_choice=((order_processed,"order_processed"),
                  (order_delivered,"order_processed"),
                  (order_processed,"order_processed"))
                
    order_status=models.IntegerField(choices=status_choice,default=cart_stage)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    products=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')