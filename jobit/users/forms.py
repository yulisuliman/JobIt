from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    profession = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=50, required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth = forms.DateField()


    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'gender', 'date_of_birth', 'profession', 'address', 'password1', 'password2']
