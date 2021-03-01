from django.db import models
from users.models import ModelTemplate
from unit.models import Product_category
# Create your models here.

class Cabinet(ModelTemplate):
    name=models.CharField(max_length=50,default=None)
    column=models.IntegerField()
    row=models.IntegerField()
    
    class Meta:
        ordering = ['created_date']


class Lockers(ModelTemplate):
    location=models.CharField(max_length=20,null=True) #位置
    code=models.CharField(max_length=20,null=True)  #編號
    name=models.CharField(max_length=50,null=True)  #名稱
    mode=models.CharField(max_length=50,null=True)  #
    # lock_time=models.IntegerField()             
    Cabinet_id=models.ForeignKey(Cabinet,on_delete=models.CASCADE,null=False) # 櫃子名稱
    Pro_cate_id=models.ForeignKey(Product_category,on_delete=models.CASCADE,null=True) # 產品分類
    status=models.BooleanField(default=False) # 是否開啟

    class Meta:
        ordering = ['created_date']

