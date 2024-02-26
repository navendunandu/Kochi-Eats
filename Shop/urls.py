from django.urls import path,include
from Shop import views 
from Shop.models import *


app_name = "webshop"
urlpatterns = [
    path('ShopHomePage/',views.ShopHomePage,name='ShopHomePage'),
    path('Food/',views.Food,name='Food'),
    path('Del_food/<int:did>',views.del_food,name='Del_food'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Request/',views.Request,name='Request'),
    path('AjaxStreet/',views.AjaxStreet,name="AjaxStreet"),
    path('AjaxSlot/',views.AjaxSlot,name="AjaxSlot"),
    path('ViewStatus/',views.ViewStatus,name="ViewStatus"),
    path('Renewal/',views.RenewalRequest,name="Renewal"),
    path('ViewRenewal/',views.ViewRenewalRequest,name="ViewRenewal"),
    path('Tables/',views.Table,name="Tables"),
    path('ViewBooking/',views.ViewBooking,name="ViewBooking"),
    path('AcceptBooking/<int:did>',views.AcceptBooking,name="AcceptBooking"),
    path('RejectBooking/<int:did>',views.RejectBooking,name="RejectBooking"),
]