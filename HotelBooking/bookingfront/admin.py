from django.contrib import admin
from .models import Reservation, RoomType, Plan

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'meal_included']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_type', 'plan', 'reservation_date']
    list_filter = ['room_type', 'plan']
