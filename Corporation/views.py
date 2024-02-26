from django.shortcuts import render,redirect
from Admin.models import *
from Shop.models import *
from Guest.models import *
import datetime

# Create your views here.
def CorporationHomePage(request):
    return render(request,'Corporation/CorporationHomePage.html')

def MyProfile(request):
    corporation=tbl_corporation.objects.get(id=request.session['cid'])
    return render(request,'Corporation/MyProfile.html',{'corporation':corporation})

def EditProfile(request):
    corporation=tbl_corporation.objects.get(id=request.session['cid'])
    if request.method == "POST":
        corporation.corporation_name=request.POST.get("txt_name")
        corporation.corporation_contact=request.POST.get("txt_contact")
        corporation.corporation_email=request.POST.get("txt_email")
        corporation.corporation_address=request.POST.get("txt_address")
        corporation.save()
        return render(request,'corporation/EditProfile.html',{'corporation':corporation})
    else:
        return render(request,'corporation/EditProfile.html',{'corporation':corporation})

def ChangePassword(request):
    corporation=tbl_corporation.objects.get(id=request.session['cid'])
    if request.method=="POST":
        cpass=request.POST.get("txt_currentpassword")
        if corporation.corporation_password == cpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass == conpass:
                corporation.corporation_password=newpass
                corporation.save()
                msg="successfully password changed"
                return render(request,'Corporation/CorporationHomePage.html',{'msg':msg})
            else:
                msg="check the entered passwords"
                return render(request,'Corporation/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Corporation/ChangePassword.html',{'msg':msg})
    else:
          return render(request,'Corporation/ChangePassword.html')
                
def ViewRequest(request):
    req=tbl_request.objects.all()
    return render(request,'Corporation/ViewRequest.html',{'request':req })
   
def up_request(request,did):
    uprequest=tbl_request.objects.get(id=did)
    disrequest=tbl_request.objects.all()
    uprequest.request_status=1
    uprequest.save()
    return redirect('webcorporation:ViewRequest')
        # return render(request,"Corporation/ViewRequest.html",{'Pdata':disrequest})
    # else:
    #     return redirect('webcorporation:ViewRequest')

def reject_request(request,did):
    rejectrqst=tbl_request.objects.get(id=did)
    disrequest=tbl_request.objects.all()
    rejectrqst.request_status=2
    rejectrqst.save()
    return redirect('webcorporation:ViewRequest')
    # else:
    #     return redirect('webcorporation:ViewRequest')

def issue_license(request,did):
    rejectrqst=tbl_request.objects.get(id=did)
    disrequest=tbl_request.objects.all()
    rejectrqst.request_status=5
    rejectrqst.save()
    return redirect('webcorporation:ViewRequest')

def issue_license_no(request,did):
    reqdata=tbl_request.objects.get(id=did)
    shopid=reqdata.shop_id
    data=tbl_shopregistration.objects.get(id=shopid.id)
    if request.method=='POST':
        data.shop_liscence=request.POST.get("txtlicense")
        data.shop_liscencedate=datetime.date.today()
        data.shop_status=1
        data.save()
        return redirect('webcorporation:ViewRequest')
    else:
        return render(request,'Corporation/IssueLicense.html')

def view_renewal(request):
    data=tbl_renewal.objects.all()
    return render(request, 'Corporation/ViewRenewal.html', {'data':data})

def renew_accpt(request,did):
    data=tbl_renewal.objects.get(id=did)
    data.renewal_status=1
    data.save()
    return redirect('webcorporation:Renewals')
    # return render(request, 'Corporation/ViewRenewal.html', {'data':data})

def renew_rej(request,did):
    data=tbl_renewal.objects.get(id=did)
    data.renewal_status=2
    data.save()
    return redirect('webcorporation:Renewals')
    # return render(request, 'Corporation/ViewRenewal.html', {'data':data})

def renew_license(request,did):
    data=tbl_renewal.objects.get(id=did)
    shopid=data.shop_id
    shopdata=tbl_shopregistration.objects.get(id=shopid.id)
    data.renewal_status=5
    shopdata.shop_status=1
    shopdata.shop_liscencedate=datetime.date.today()
    shopdata.save()
    data.save()
    return redirect('webcorporation:Renewals')

        

    



    