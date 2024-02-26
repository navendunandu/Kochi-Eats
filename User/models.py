from django.db import models
from Guest.models import *
from Shop.models import *



# Create your models here.
class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_fordate=models.CharField(max_length=10)
    booking_fortime=models.CharField(max_length=10)
    booking_count=models.CharField(max_length=10)
    booking_amount=models.CharField(max_length=10)
    booking_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    shop=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE, null=True)

# class tbl_cart(models.Model):
#     food_quantity=models.CharField(max_length=10)
#     cart_status=models.IntegerField(default=0)
#     food=models.ForeignKey(tbl_food,on_delete=models.CASCADE)
#     booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=10)
    complaint_description=models.CharField(max_length=10)
    complaint_reply=models.CharField(max_length=10)
    shop=models.ForeignKey(tbl_shopregistration,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)


class tbl_rating(models.Model):
    user_rating=models.CharField(max_length=10)
    user_review=models.CharField(max_length=10)
    review_date=models.CharField(max_length=10)
    food=models.ForeignKey(tbl_food,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    
