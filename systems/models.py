from django.db import models
from users.models import ModelTemplate

# Create your models here.

DRAWER_MOD=[
    ('dra', 'drawer'),
    ('pro_cate', 'pro_cate'),
]

class Information(ModelTemplate):
    name=models.CharField(max_length=50,default=None)
    value=models.CharField(max_length=50,default=None)

    class Meta:
        ordering = ['created_date']

class Configuration(ModelTemplate):
    # drawer_mod=models.CharField(max_length=50,choices=ACCTYPE_CHICES)
    drawer_mod=models.CharField(max_length=50,choices=DRAWER_MOD,default="dra")

    class Meta:
        ordering = ['created_date']
