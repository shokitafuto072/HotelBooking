from django.urls import path
from . import views  # views をインポート

app_name = 'bookingback'


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('checkinlist/',views.checkinlist,name="checkinlist"),
    path('checkoutlist/',views.checkoutlist,name="checkoutlist"),
    path('guests_list/',views.guests_list,name="guests_list"),
    path('clean_manage/',views.clean_manage,name="clean_manage"),
    path('kyakusitu/',views.kyakusitu,name="kyakusitu"),
    path('edit_plans/',views.edit_plans,name="edit_plans"),
    path('shukei/',views.shukei,name="shukei"),
    path('room_status/',views.room_status,name="room_status"),



]
