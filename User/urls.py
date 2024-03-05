from django.urls import path,include
from User import views

app_name="webuser"

urlpatterns = [
    path('',views.UserHomePage,name='UserHomePage'),
    path('UserBooking/',views.UserBooking,name='UserBooking'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('UserMyProfile/',views.UserMyProfile,name='UserMyProfile'),
    path('UserEditProfile/',views.UserEditProfile,name='UserEditProfile'),
    path('UserChangePassword/',views.UserChangePassword,name='UserChangePassword'),
    path('SearchShop/',views.SearchShop,name='SearchShop'),
    path('AjaxShop/',views.AjaxShop,name='AjaxShop'),
    path('AjaxSearch/',views.AjaxSearch,name='AjaxSearch'),
    path('TableBooking/<int:id>',views.ShopTable,name='TableBooking'),
    path('Payment/<int:id>',views.Payment,name='Payment'),
    path('Success/',views.Success,name='Success'),
]