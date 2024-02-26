from django.shortcuts import render,redirect
from Admin.models import tbl_place
from Guest.models import *
# Create your views here.

def index(request):
    return render(request, 'Guest/index.html')

def userregistration(request):
    placedata=tbl_place.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        gender=request.POST.get("txt_gender")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("txt_place"))
        tbl_newuser.objects.create(user_name=name,user_contact=contact,user_email=email,user_gender=gender,user_address=address,user_photo=photo,user_password=password,place=placeid)

        return render(request,'Guest/UserRegistration.html',{'Pdata':placedata})
    else:

        return render(request,'Guest/UserRegistration.html',{'Pdata':placedata})


def shopregistration(request):
    placedata=tbl_place.objects.all()
    streetdata=tbl_street.objects.all()
    if request.method=="POST" and request.FILES:
        sname=request.POST.get("txt_shopname")
        liscence=request.POST.get("txt_shopliscence")
        scontact=request.POST.get("txt_shopcontact")
        semail=request.POST.get("txt_shopemail")
        saddress=request.POST.get("txt_shopaddress")
        sphoto=request.FILES.get("txt_shopphoto")
        oname=request.POST.get("txt_ownername")
        ophoto=request.FILES.get("txt_ownerphoto")
        proof=request.FILES.get("txt_proof")
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("txt_place"))
        streetid=tbl_street.objects.get(id=request.POST.get("txt_street"))
        tbl_shopregistration.objects.create(shop_name=sname,
        shop_liscence=liscence,
        shop_contact=scontact,
        shop_email=semail,
        shop_address=saddress,
        shop_photo=sphoto,
        owner_name=oname,
        owner_photo=ophoto,
        owner_proof=proof,
        shop_password=password,
        place=placeid,
        street=streetid)

        return render(request,'Guest/ShopRegistration.html',{'Pdata':placedata,'Sdata':streetdata})
    else:

        return render(request,'Guest/ShopRegistration.html',{'Pdata':placedata,'Sdata':streetdata})

def login(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Pass=request.POST.get('txt_password')
        ucount=tbl_newuser.objects.filter(user_email=Email,user_password=Pass).count()
        scount=tbl_shopregistration.objects.filter(shop_email=Email,shop_password=Pass).count()
        hcount=tbl_health.objects.filter(health_email=Email,health_password=Pass).count()
        cocount=tbl_corporation.objects.filter(corporation_email=Email,corporation_password=Pass).count()

        acount=tbl_admin.objects.filter(admin_email=Email,admin_password=Pass).count()

        if ucount > 0:
            userdata=tbl_newuser.objects.get(user_email=Email,user_password=Pass)
            request.session['uid']=userdata.id
            return redirect('webuser:UserHomePage')
        elif scount > 0:
            shopdata=tbl_shopregistration.objects.get(shop_email=Email,shop_password=Pass)
            request.session['sid']=shopdata.id
            return redirect('webshop:ShopHomePage')
        elif cocount > 0:
            coopdata=tbl_corporation.objects.get(corporation_email=Email,corporation_password=Pass)
            request.session['cid']=coopdata.id
            return redirect('webcorporation:CorporationHomePage')
        elif hcount > 0:
            heldata=tbl_health.objects.get(health_email=Email,health_password=Pass)
            request.session['hid']=heldata.id
            return redirect('webhealth:HealthHomePage')
        elif acount > 0:
            adata=tbl_admin.objects.get(admin_email=Email,admin_password=Pass)
            request.session['aid']=adata.id
            return redirect('webadmin:AdminHomePage')
        else:
            msg="Invalid Credentials!!"
            return render(request,'Guest/Login.html',{'msg':msg})
    else:
        return render(request,'Guest/Login.html')
        

