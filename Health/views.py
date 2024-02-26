from django.shortcuts import render,redirect
from Admin.models import *
from Shop.models import *

# Create your views here.
def HealthHomePage(request):
    return render(request,'Health/HealthHomePage.html')

def MyProfile(request):
    health=tbl_health.objects.get(id=request.session['hid'])
    return render(request,'Health/MyProfile.html',{'health':health})

def EditProfile(request):
    health=tbl_health.objects.get(id=request.session['hid'])
    if request.method == "POST":
        health.health_name=request.POST.get("txt_name")
        health.health_contact=request.POST.get("txt_contact")
        health.health_email=request.POST.get("txt_email")
        health.health_address=request.POST.get("txt_address")
        health.save()
        return render(request,'Health/EditProfile.html',{'health':health})
    else:
        return render(request,'Health/EditProfile.html',{'health':health})

def ChangePassword(request):
    health=tbl_health.objects.get(id=request.session['hid'])
    if request.method=="POST":
        cpass=request.POST.get("txt_currentpassword")
        if health.health_password == cpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass == conpass:
                health.health_password=newpass
                health.save()
                msg="successfully password changed"
                return render(request,'Health/ChangePassword.html',{'msg':msg})
            else:
                msg="check the entered passwords"
                return render(request,'Health/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Health/ChangePassword.html',{'msg':msg})
    else:
          return render(request,'Health/ChangePassword.html')
                

def ViewShopAccepted(request):
    req=tbl_request.objects.all()
    return render(request,'Health/ViewShopAccepted.html',{'request':req })

def Accept_request  (request,did):
    uprequest=tbl_request.objects.get(id=did)
    disrequest=tbl_request.objects.all()
    uprequest.request_status=3
    uprequest.save()
    return redirect('webhealth:ViewShopAccepted')
        # return render(request,"Corporation/ViewRequest.html",{'Pdata':disrequest})
    # else:
    #     return redirect('webcorporation:ViewRequest')

def Reject_request(request,did):
    rejectrqst=tbl_request.objects.get(id=did)
    disrequest=tbl_request.objects.all()
    rejectrqst.request_status=4
    rejectrqst.save()
    return redirect('webhealth:ViewShopAccepted')
    # else:

def RenewalReq(request):
    req=tbl_renewal.objects.all()
    return render(request,'Health/RenewalRequest.html',{'data':req })

def Renewal_Accept_request  (request,did):
    uprequest=tbl_renewal.objects.get(id=did)
    uprequest.renewal_status=3
    uprequest.save()
    return redirect('webhealth:RenewalReq')

def Renewal_Reject_request(request,did):
    rejectrqst=tbl_renewal.objects.get(id=did)
    rejectrqst.renewal_status=4
    rejectrqst.save()
    return redirect('webhealth:RenewalReq')