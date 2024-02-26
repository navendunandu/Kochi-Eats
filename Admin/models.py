from django.db import models

# Create your models here.
class tbl_place(models.Model):
    place_name=models.CharField(max_length=10)

class tbl_street(models.Model):
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    street_name=models.CharField(max_length=10)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=10)
    admin_email=models.CharField(max_length=10)
    admin_password=models.CharField(max_length=10)

class tbl_corporation(models.Model):
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    corporation_name=models.CharField(max_length=10)
    corporation_email=models.CharField(max_length=10)
    corporation_contact=models.CharField(max_length=10)
    corporation_address=models.CharField(max_length=10)
    corporation_password=models.CharField(max_length=10)

class tbl_health(models.Model):
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    health_name=models.CharField(max_length=10)
    health_email=models.CharField(max_length=10)
    health_contact=models.CharField(max_length=10)
    health_address=models.CharField(max_length=10)
    health_password=models.CharField(max_length=10)

class tbl_slot(models.Model):
    street=models.ForeignKey(tbl_street,on_delete=models.CASCADE)
    slot_number=models.CharField(max_length=10)
    shop_status=models.IntegerField(default=0)  


