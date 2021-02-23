from django.db import models
from users.models import ModelTemplate,Departments

# Create your models here.

class Unit(ModelTemplate):
    name=models.CharField(max_length=50,default=None)

    class Meta:
        ordering = ['created_date']

class Product_category(ModelTemplate):
    name=models.CharField(max_length=50,default=None)
    code=models.CharField(max_length=50,default=None)
    Departments_id=models.ForeignKey(Departments,on_delete=models.CASCADE)


    class Meta:
        ordering = ['created_date']

