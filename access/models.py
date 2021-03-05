from django.db import models
from users.models import ModelTemplate,Profiles
from unit.models import Product_category
from locker.models import Lockers


# Create your models here.

class Functions(ModelTemplate):
    active=models.BooleanField(default=True)
    name=models.CharField(max_length=50,default=None)

    class Meta:
        ordering = ['created_date']

class UI_access(ModelTemplate):
    name=models.CharField(max_length=100,default=None)
    Profiles_id=models.ForeignKey(Profiles,on_delete=models.CASCADE)
    Functions_id=models.ForeignKey(Functions,on_delete=models.CASCADE,null=True)
    perm_read=models.BooleanField(default=True)
    perm_unlink=models.BooleanField(default=True)
    perm_write=models.BooleanField(default=True)
    perm_create=models.BooleanField(default=True)

    class Meta:
        ordering = ['created_date']

class Locker_access(ModelTemplate):
    Profiles_id=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    active=models.BooleanField(default=True)
    Lockers_ids=models.ManyToManyField(Lockers,blank=True)

    class Meta:
        ordering=['created_date']

class category_access(ModelTemplate):
    Profiles_ids=models.ManyToManyField(Profiles,blank=True)
    Pro_cate_id=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    Lockers_ids=models.ManyToManyField(Lockers,blank=True)

    class Meta:
        ordering=['created_date']