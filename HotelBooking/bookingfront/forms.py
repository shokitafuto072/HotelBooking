from django import forms
from .models import Reservation, Plan, RoomType, RoomAllocation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room_type', 'reservation_date', 'plan','payment_method']

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'plan_price', 'meal_included']

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name', 'room_price','reservation_date',]

class RoomAllocationForm(forms.ModelForm):
    class Meta:
        model = RoomAllocation
        fields = ['room_type','room_number','room_price']

