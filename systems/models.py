from django.db import models
from users.models import ModelTemplate

# Create your models here.

DRAWER_MOD=[
    ('dra', 'drawer'),
    ('pro_cate', 'pro_cate'),
]

class Information(ModelTemplate):
    IP=models.CharField(max_length=50,default=None)
    name=models.CharField(max_length=50,default=None)
    manufacture_date=models.DateField(default=None)
    kind=models.CharField(max_length=50,default=None)
    machine_NO=models.CharField(max_length=50,default=None)
    guarantee_date=models.DateField(default=None)
    soft_NO=models.CharField(max_length=50,default=None)
    
    class Meta:
        ordering = ['created_date']

class Configuration(ModelTemplate):
    # drawer_mod=models.CharField(max_length=50,choices=ACCTYPE_CHICES)
    drawer_mod=models.CharField(max_length=50,choices=DRAWER_MOD,default="dra")

    class Meta:
        ordering = ['created_date']
