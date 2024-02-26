from django.urls import path,include
from Admin import views

app_name = "webadmin"

urlpatterns = [
    path('place/',views.place,name='Place'),
    path('street/',views.street,name='street'),
    path('CorporationRegistration/',views.corporationregistration,name='corporationregistration'),
    path('del_place/<int:did>',views.del_place,name='Del_place'),
    path('Update_place/<int:did>',views.up_place,name='Update_place'),
    path('del_street/<int:did>',views.del_street,name='Del_street'),
    path('Update_street/<int:did>',views.up_street,name='Update_street'),
    path('HealthRegistration/',views.healthregistration,name='healthregistration'),
    path('AdminHomePage/',views.AdminHomePage,name='AdminHomePage'),
    path('AdminMyProfile/',views.AdminMyProfile,name='AdminMyProfile'),
    path('Slot/',views.Slot,name='Slot'),






    


    


]