from django.urls import path,include
from Health import views


app_name = "webhealth"
urlpatterns = [
    path('HealthHomePage/',views.HealthHomePage,name='HealthHomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('ViewShopAccepted/',views.ViewShopAccepted,name='ViewShopAccepted'),
    path('Accept_request/<int:did>',views.Accept_request,name='Accept_request'),
    path('Reject_request/<int:did>',views.Reject_request,name='Reject_request'),
    path('RenewalReq/',views.RenewalReq,name='RenewalReq'),
    path('RenewalReqAccpt/<int:did>',views.Renewal_Accept_request,name='RenewalReqAccpt'),
    path('RenewalReqRej/<int:did>',views.Renewal_Reject_request,name='RenewalReqRej'),

    

    


]