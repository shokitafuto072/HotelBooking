from django.contrib import admin
from .models import Reservation, RoomType, Plan, RoomAllocation

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'room_price']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'plan_price', 'meal_included']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_type', 'plan', 'reservation_date','payment_method']
    list_filter = ['room_type', 'plan','payment_method']

class RoomAllocationAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'room_type', 'room_price', 'reservation_user']
    fields = ['reservation', 'room_type', 'room_number', 'room_price', 'description', 'first_name', 'last_name']  # 必要なフィールドのみ表示

    # reservation に紐づいた user の情報を表示するカスタムメソッド
    def reservation_user(self, obj):
        return obj.reservation.user if obj.reservation else None
    reservation_user.short_description = 'User'

admin.site.register(RoomAllocation, RoomAllocationAdmin)