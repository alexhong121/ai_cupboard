from django.db import models
from users.models import ModelTemplate
from unit.models import Product_category
from locker.models import Lockers

# Create your models here.

class Product(ModelTemplate):
    active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='images/inv/',default="")
    name=models.CharField(max_length=50,default=None)
    code=models.CharField(max_length=20,default=None,null=True)
    form=models.CharField(max_length=100,default=None,null=True)
    attribute=models.CharField(max_length=50,default=None,null=True)
    Product_cate_id=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    remark=models.CharField(max_length=200,default=None,null=True)
    Lockers_id=models.ForeignKey(Lockers,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['created_date']

class Stock(ModelTemplate):
    initial_value=models.IntegerField(default=0)
    out_value=models.IntegerField(default=0)
    in_value=models.IntegerField(default=0)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    remark=models.CharField(max_length=200,default=None,null=True)

    class Meta:
        ordering=['created_date']
