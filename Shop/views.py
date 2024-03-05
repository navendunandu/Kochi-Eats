from django.shortcuts import render,redirect
from Guest.models import  *
from Admin.models import *
from Shop.models import *
from User.models import *
from datetime import datetime, timedelta
# Create your views here.
def ShopHomePage(request):
    shopdata = tbl_shopregistration.objects.get(id=request.session['sid'])
    
    if shopdata.shop_liscencedate is not None and shopdata.shop_liscencedate != '':
        registered_date = shopdata.shop_liscencedate
        expiry_date = registered_date + timedelta(days=365)
        
        if expiry_date <= datetime.now().date():
            shopdata.shop_status = 2
            shopdata.save()
            return render(request, 'Shop/ShopHomePage.html', {'msg': 'License Expired', 'data': shopdata})
    
    return render(request, 'Shop/ShopHomePage.html', {'data': shopdata})

def Food(request):
    fdata=tbl_food.objects.all()
    shop=tbl_shopregistration.objects.get(id=request.session['sid'])
    if request.method=="POST":
        name=request.POST.get("txt_foodname")
        photo=request.FILES.get("txt_foodphoto")
        rate=request.POST.get("txt_foodrate")
        description=request.POST.get("txt_fooddescription")
        tbl_food.objects.create(food_name=name,
        food_photo=photo,
        food_rate=rate,
        food_description=description,
        shop=shop,
        )
        return render(request,'Shop/Food.html',{'fdata':fdata})
    else:
        return render(request,'Shop/Food.html',{'fdata':fdata})

def del_food(request,did):
    tbl_food.objects.get(id=did).delete()
    return redirect('webshop:Food')


    
def MyProfile(request):
    shop=tbl_shopregistration.objects.get(id=request.session['sid'])
    return render(request,'Shop/MyProfile.html',{'shop':shop})

def EditProfile(request):
    shop=tbl_shopregistration.objects.get(id=request.session['sid'])
    if request.method == "POST":
        shop.shop_name=request.POST.get("txt_name")
        shop.shop_contact=request.POST.get("txt_contact")
        shop.shop_email=request.POST.get("txt_email")
        shop.shop_address=request.POST.get("txt_address")
        shop.save()
        return render(request,'Shop/EditProfile.html',{'shop':shop})
    else:
        return render(request,'Shop/EditProfile.html',{'shop':shop})

def ChangePassword(request):
    shop=tbl_shopregistration.objects.get(id=request.session['sid'])
    if request.method=="POST":
        cpass=request.POST.get("txt_currentpassword")
        if shop.shop_password == cpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass == conpass:
                shop.shop_password=newpass
                shop.save()
                msg="successfully password changed"
                return render(request,'Shop/ShopHomePage.html',{'msg':msg})
            else:
                msg="check the entered passwords"
                return render(request,'Shop/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Shop/ChangePassword.html',{'msg':msg})
    else:
          return render(request,'Shop/ChangePassword.html')



def Request(request):
    slot=tbl_slot.objects.all()
    street=tbl_street.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        tbl_request.objects.create(shop_id=tbl_shopregistration.objects.get(id=request.session['sid']),
                                    slot_id=tbl_slot.objects.get(id=request.POST.get("txtslot")))
        return render(request,'Shop/Request.html',{'Data':slot,'StreetData':street,'Pdata':place})
    else:
        return render(request,'Shop/Request.html',{'Data':slot,'StreetData':street,'Pdata':place})



def AjaxStreet(request):
    disob=tbl_place.objects.get(id=request.GET.get('STREET'))
    street=tbl_street.objects.filter(place=disob)
    return render(request,'User/AjaxShop.html',{'disstreet':street})

def AjaxSlot(request):
    disob=tbl_street.objects.get(id=request.GET.get('SLOT'))
    slot=tbl_slot.objects.filter(street_id=disob)
    return render(request,'Shop/AjaxSlot.html',{'slot':slot})
       
def ViewStatus(request):
    status = tbl_request.objects.all()
    return render(request,'Shop/ViewStatus.html',{'status':status})

def RenewalRequest(request):
    shopdata=tbl_shopregistration.objects.get(id=request.session['sid'])
    tbl_renewal.objects.create(shop_id=shopdata)
    return render(request, 'Shop/ShopHomePage.html', {'rmsg':'Renewal Application Sended'})

def ViewRenewalRequest(request):
    shopdata=tbl_shopregistration.objects.get(id=request.session['sid'])
    renewaldata=tbl_renewal.objects.filter(shop_id=shopdata)
    return render(request, 'Shop/RenewalRequest.html', {'data':renewaldata})

def Table(request):
    table=tbl_tables.objects.all()
    shop=tbl_shopregistration.objects.get(id=request.session['sid'])
    if request.method=="POST":
        count=request.POST.get("txttable")
        tbl_tables.objects.create(table_count=count,
        shop_id=shop,
        )
        return render(request,'Shop/ShopTables.html',{'table':table})
    else:
        return render(request,'Shop/ShopTables.html',{'table':table})

def ViewBooking(request):
    shopdata=tbl_shopregistration.objects.get(id=request.session['sid'])
    booking=tbl_booking.objects.filter(shop=shopdata)
    return render(request,'Shop/ViewBookings.html',{'data':booking})

def AcceptBooking(request,did):
    data=tbl_booking.objects.get(id=did)
    data.booking_status=1
    data.save()
    return render(request,'Shop/ViewBookings.html',{'msg':'Booking Accepted'})

def RejectBooking(request,did):
    data=tbl_booking.objects.get(id=did)
    data.booking_status=2
    data.save()
    return render(request,'Shop/ViewBookings.html',{'msg':'Booking Rejected'})