from django.db import models
from Admin.models import *

# Create your models here.
class tbl_newuser(models.Model):
    user_name=models.CharField(max_length=10)
    user_contact=models.CharField(max_length=20)
    user_email=models.EmailField()
    user_gender=models.CharField(max_length=20)
    user_address=models.TextField()
    user_photo=models.FileField(upload_to='UserDocs/')
    user_password=models.CharField(max_length=20)
    user_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)


class tbl_shopregistration(models.Model):
    shop_name=models.CharField(max_length=10)
    shop_liscence=models.CharField(max_length=15,null=True)
    shop_contact=models.CharField(max_length=10)
    shop_email=models.CharField(max_length=10)
    shop_address=models.CharField(max_length=10)
    shop_photo=models.FileField(upload_to='UserDocs/')
    owner_name=models.CharField(max_length=10)
    owner_photo=models.FileField(upload_to='UserDocs/')
    owner_proof=models.FileField(upload_to='UserDocs/')
    shop_password=models.CharField(max_length=10)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    street=models.ForeignKey(tbl_street,on_delete=models.CASCADE)
    shop_status=models.IntegerField(default=0)  
    shop_liscencedate=models.DateField(null=True)