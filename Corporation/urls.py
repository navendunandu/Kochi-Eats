from django.urls import path,include
from Corporation import views


app_name = "webcorporation"
urlpatterns = [
    path('CorporationHomePage/',views.CorporationHomePage,name='CorporationHomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('ViewRequest/',views.ViewRequest,name='ViewRequest'),
    path('Accept_request/<int:did>',views.up_request,name='Accept_request'),
    path('Reject_request/<int:did>',views.reject_request,name='Reject_request'),
    path('Issue_license/<int:did>',views.issue_license,name='Issue_license'),
    path('Issue_license_no/<int:did>',views.issue_license_no,name='Issue_license_no'),
    path('Renewals/',views.view_renewal,name='Renewals'),
    path('AccptRenewals/<int:did>',views.renew_accpt,name='AccptRenewals'),
    path('RejRenewals/<int:did>',views.renew_rej,name='RejRenewals'),
    path('RenewLic/<int:did>',views.renew_license,name='RenewLic'),

    





]