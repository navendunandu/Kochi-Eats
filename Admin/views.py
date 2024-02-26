from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
def place(request):
    pdata=tbl_place.objects.all()
    if request.method=="POST":
        tbl_place.objects.create(place_name=request.POST.get("txt_place")) #to insert data into the tbl
        return render(request,'Admin/Place.html',{'Pdata':pdata })
    else:
        return render(request,'Admin/Place.html',{'Pdata':pdata})
       
def del_place(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('webadmin:Place')

def up_place(request,did):
    upplace=tbl_place.objects.get(id=did)
    displace=tbl_place.objects.all()
    if request.method=="POST":
        upplace.place_name=request.POST.get("txt_place")
        upplace.save()
        return render(request,"Admin/Place.html",{'Pdata':displace})
    else:
        return render(request,'Admin/Place.html',{'Pdata':displace,'udata':upplace})


def street(request):
    
    selobj=tbl_place.objects.all()
    Sdata=tbl_street.objects.all()
    if request.method=="POST":
        
        tbl_street.objects.create(street_name=request.POST.get("txt_street"),place_id=request.POST.get("select"))
        return render(request,'Admin/Street.html',{'Data':selobj,'Sdata':Sdata})
    else:
        return render(request,'Admin/Street.html',{'Data':selobj,'Sdata':Sdata})

def del_street(request,did):
    tbl_street.objects.get(id=did).delete()
    return redirect('webadmin:street')

def up_street(request,did):
    upstreet=tbl_street.objects.get(id=did)
    disstreet=tbl_street.objects.all()
    selobj=tbl_place.objects.all()
    if request.method=="POST":
        upstreet.street_name=request.POST.get("txt_street")
        upstreet.save()
        return render(request,"Admin/Street.html",{'Sdata':disstreet})
    else:
        return render(request,'Admin/Street.html',{'Sdata':disstreet,'udata':upstreet,'Data':selobj})

def corporationregistration(request):
    placedata=tbl_place.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        address=request.POST.get("txt_address")  
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("txt_place"))
        tbl_corporation.objects.create(corporation_name=name,
        corporation_contact=contact,
        corporation_email=email,
        corporation_address=address,
        corporation_password=password,
        place=placeid)

        return render(request,'Admin/CorporationRegistration.html',{'Pdata':placedata})
    else:

        return render(request,'Admin/CorporationRegistration.html',{'Pdata':placedata})



def healthregistration(request):
    placedata=tbl_place.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        address=request.POST.get("txt_address")  
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("txt_place"))
        tbl_health.objects.create(health_name=name,
        health_contact=contact,
        health_email=email,
        health_address=address,
        health_password=password,
        place=placeid)

        return render(request,'Admin/HealthRegistration.html',{'Pdata':placedata})
    else:

        return render(request,'Admin/HealthRegistration.html',{'Pdata':placedata})

def AdminHomePage(request):
        return render(request,'Admin/AdminHomePage.html')


def AdminMyProfile(request):
    admin=tbl_admin.objects.get(id=request.session['uid'])
    return render(request,'Wadmin/AdminMyProfile.html',{'admin':admin})

def Slot(request):
    Seldata=tbl_street.objects.all()
    Sdata=tbl_slot.objects.all()
    if request.method=="POST":
        tbl_slot.objects.create(slot_number=request.POST.get("txt_slotnumber"),street_id=request.POST.get("select"))
        return render(request,'Admin/Slot.html',{'Streetdata':Seldata})
    else:
        return render(request,'Admin/Slot.html',{'Streetdata':Seldata})







