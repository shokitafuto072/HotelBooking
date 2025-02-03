from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'room_type', 'reservation_date', 'plan', 'first_name', 'last_name', 'email', 'birth_date', 'postal_number', 'address']
