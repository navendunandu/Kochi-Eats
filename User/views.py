from django.shortcuts import render
from Guest.models import *
from User.models import *
# Create your views here.
def UserHomePage(request):
    return render(request,'User/UserHomePage.html')

def UserBooking(request):
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    booking=tbl_booking.objects.filter(user=userdata)
    return render(request,'User/UserBooking.html',{'data':booking})

def Complaint(request):
    cdata=tbl_complaint.objects.all()
    user=tbl_newuser.objects.get(id=request.session['uid'])
    shop=tbl_shopregistration.objects.get(id=request.session['sid'])
    if request.method=="POST":
        title=request.POST.get("txt_title")
        description=request.POST.get("txt_description")
        tbl_complaint.objects.create(complaint_title=title,
        complaint_description=description,
        user=user,
        shop=shop,
        )
        return render(request,'User/Complaint.html',{'cdata':cdata})
    else:
        return render(request,'User/Complaint.html',{'cdata':cdata})


def UserMyProfile(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,'User/UserMyProfile.html',{'user':user})


def UserEditProfile(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method == "POST":
        user.user_name=request.POST.get("txt_name")
        user.user_contact=request.POST.get("txt_contact")
        user.user_email=request.POST.get("txt_email")
        user.user_address=request.POST.get("txt_address")
        user.save()
        return render(request,'User/UserEditProfile.html',{'user':user})
    else:
        return render(request,'User/UserEditProfile.html',{'user':user})

def UserChangePassword(request):
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        cpass=request.POST.get("txt_currentpassword")
        if user.user_password == cpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass == conpass:
                user.user_password=newpass
                user.save()
                msg="successfully password changed"
                return render(request,'User/HomePage.html',{'msg':msg})
            else:
                msg="check the entered passwords"
                return render(request,'User/UserChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'User/UserChangePassword.html',{'msg':msg})
    else:
          return render(request,'User/UserChangePassword.html')
                

def SearchShop(request):
    displace=tbl_place.objects.all()
    shop=tbl_shopregistration.objects.all()
    return render(request,'User/SearchShop.html',{'displace':displace,'shop':shop})

def ShopTable(request, id):
    shop = tbl_shopregistration.objects.get(id=id)
    user=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=='POST':
        date = request.POST.get('txtdate')
        time = request.POST.get('txttime')
        count = request.POST.get('txtcount')
        tbl_booking.objects.create(
            booking_fordate=date,
            booking_fortime=time,
            booking_count=count,
            user=user,
            shop=shop,
        )
        return render(request, 'User/TableBooking.html', {'msg':'Booking Requested'})
    return render(request, 'User/TableBooking.html')
                
def AjaxShop(request):
    disob=tbl_place.objects.get(id=request.GET.get('STREET'))
    street=tbl_street.objects.filter(place=disob)
    return render(request,'User/AjaxShop.html',{'disstreet':street})

def AjaxSearch(request):
    disob=tbl_street.objects.get(id=request.GET.get('SHOP'))
    shop=tbl_shopregistration.objects.filter(street=disob)
    return render(request,'User/AjaxSearch.html',{'shop':shop})


