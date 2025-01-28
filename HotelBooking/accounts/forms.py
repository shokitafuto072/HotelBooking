from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "postal_number",
            "address",    
       
        )
        widgets = {
            'birth_date': DateInput(),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user

class LoginFrom(AuthenticationForm):

    class Meta:
        model = User

