from django.urls import path,include
from Guest import views
app_name="webguest"
urlpatterns = [
    path('',views.index,name="index"),
    path('UserRegistration/',views.userregistration,name='userregistration'),
    path('ShopRegistration/',views.shopregistration,name='shopregistration'),
    path('Login/',views.login,name='login'),
]