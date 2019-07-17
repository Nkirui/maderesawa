from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, DriverProfile, StaffProfile, Saccoowner, SaccoProfile

"""
A form for the driver to signup,this form would not require much details as they would
 not interact much with application.
"""


class AnonymousSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


    def save(self, commit=True):
       # user = super().save(commit=False)
        user = super(AnonymousSignUpForm, self).save(commit=False)
        user.is_saccodriver = True
        if commit:
            user.save()
        return user


class SaccoOwnerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class StaffSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

        def save(self, commit=True):
            user = super(StaffSignupForm, self).save(commit=False)
            # user = super().save(commit=False)
            user.is_staff = True

            if commit:
                user.save()
            return user


class DriverForm(forms.ModelForm):
    class Meta:
        model = DriverProfile

        exclude = ('employer','user','user_owner','emp_rmks',)


class DriverForm2(forms.ModelForm):
    class Meta:
        model = DriverProfile

        exclude = ('employer','user','user_owner',)


class OwnerProfileForm(forms.ModelForm):
    class Meta:
        model = Saccoowner
        fields = ['national_id','phone_number','address']
        #exclude = ['user','sacco_prof']



class StaffProfileForm(UserCreationForm):
    class Meta:
        model = StaffProfile

        fields = '__all__'


class SaccoProfileForm(forms.ModelForm):
    class Meta:
        model = SaccoProfile
        fields = ['sacco_name','sacco_address','sacco_phonenumber','sacco_url','town','city']