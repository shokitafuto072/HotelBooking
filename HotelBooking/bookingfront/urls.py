from django.urls import path
from . import views

app_name = 'bookingfront'

urlpatterns = [
    path('', views.room_selection, name='room_selection'),
    path('plan_selection/', views.plan_selection, name='plan_selection'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('booking_complete/', views.booking_complete, name='booking_complete'),
    #path('booking_form/', views.booking_form, name='booking_form'),
]
