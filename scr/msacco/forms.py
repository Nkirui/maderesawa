from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User, DriverProfile


class DriverSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_driver = True
        if commit:
            user.save()
        return user


class EmployerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
        return user

class DriverForm(ModelForm):
    class Meta:
        model = DriverProfile
        fields = '__all__'