from django.urls import path
from . import views

app_name = 'bookingfront'

urlpatterns = [
    
    path('yoyaku', views.yoyaku, name='yoyaku'),
    path('', views.home, name='home'),
    path('room_selection', views.room_selection, name='room_selection'),
    path('plan_selection/', views.plan_selection, name='plan_selection'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('booking_complete/', views.booking_complete, name='booking_complete'),
    #path('booking_form/', views.booking_form, name='booking_form'),

    path('dashboard',views.dashboard,name="dashboard"),
    path('checkinlist/',views.checkinlist,name="checkinlist"),
    path('checkoutlist/',views.checkoutlist,name="checkoutlist"),
    path('guests_list/',views.guests_list,name="guests_list"),
    path('clean_manage/',views.clean_manage,name="clean_manage"),
    path('kyakusitu/',views.kyakusitu,name="kyakusitu"),
    path('edit_plans/',views.edit_plans,name="edit_plans"),
    path('checkinlist/',views.shukei,name="shukei"),
    path('room_status/',views.room_status,name="room_status"),
    path('dashboard/',views.dashboard,name="dashboard"),
]
