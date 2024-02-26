from django.db import models
from Guest.models import *


# Create your models here.


class tbl_food(models.Model):
    food_name=models.CharField(max_length=10)
    food_rate=models.CharField(max_length=10)
    food_description=models.CharField(max_length=10)
    food_photo=models.FileField(upload_to='UserDocs/')
    shop=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE)



class tbl_request(models.Model):
    shop_id=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE)
    slot_id=models.ForeignKey(tbl_slot,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)

class tbl_renewal(models.Model):
    shop_id=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE)
    renewal_date=models.DateField(auto_now_add=True)
    renewal_status=models.IntegerField(default=0)

class tbl_tables(models.Model):
    shop_id=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE)
    table_count=models.CharField(max_length=10)



