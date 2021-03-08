from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#######################alex 2020/09/23 app 登录##############################

class ModelTemplate(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    create_uid= models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_create_uid",
        # related_query_name="%(app_label)s_%(class)ss",
        on_delete=models.CASCADE,null=True
    )
    written_date=models.DateTimeField(auto_now=True,null=True)
    write_uid=models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_write_uid",
        # related_query_name="%(app_label)s_%(class)ss",
        on_delete=models.CASCADE,null=True
    )

    class Meta:
        abstract=True

class Departments(ModelTemplate):
    name=models.CharField(max_length=50,default=None)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_date']

class Profiles(ModelTemplate):
    image_url=models.ImageField(upload_to='images/',null=True, blank=True)
    name=models.CharField(max_length=50,default=None)
    alias=models.CharField(max_length=50,default=None,null=True)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=50,null=True)
    remark=models.TextField(default="")
    Departments_id=models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    AuthUser_id=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ['created_date']

class Questions(ModelTemplate):
    proposition=models.CharField(max_length=50,default=None)
    
    class Meta:
        ordering = ['created_date']
        
class Quest_answers(ModelTemplate):
    Questions_id=models.ForeignKey(Questions,on_delete=models.CASCADE,null=False)
    answer=models.CharField(max_length=50,default=None)
    Profiles_id=models.ForeignKey(Profiles,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_date']
############################################################################################################