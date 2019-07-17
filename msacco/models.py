
from django.contrib.auth.models import AbstractUser
from django.db import models

from scr import settings


# To abstract the base default class.
class User(AbstractUser):
    is_saccodriver = models.BooleanField(verbose_name=('Driver status'),default=True)
    is_saccoowner = models.BooleanField(verbose_name=('Owner status'),default=True)
    #is_saccostaff = models.BooleanField(default=False,verbose_name=('staff status'),
    #                               help_text = ('Designates whether the user can log in this admin site.' ), )

    class Meta:
        verbose_name_plural = 'Users Account'



# This is the table that contains the profile details of the sacco


class Saccoowner(models.Model):
    user = models.OneToOneField(User,verbose_name='Sacco Owner', on_delete=models.CASCADE,null=True)
    national_id = models.CharField(verbose_name=("National Id or Passport"), max_length=100, blank=False)
    phone_number = models.CharField(verbose_name=("Tel"), max_length=12)
    address = models.CharField(blank=False, max_length=200, help_text='P.O Box 357')
    created_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True,null=True)


    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'The Owners Of The Sacco'

class SaccoProfile(models.Model):
    LOCATION_CHOICES = (
        ('None', "None"), ('Kasarani', "Kasarani"), ('Kawangware', "Kawangware"), ('Uthiru', "Uthiru"),
        ('Pipeline', "Pipeline"),
        ('Ngong', "Ngong"),
        ('Dohnholm', "Dohnholm"),
        ('Kilimani', "Kilimani"),
    )
    owner=models.OneToOneField(Saccoowner,on_delete=models.CASCADE,default=1,blank=True,null=True)
    sacco_name = models.CharField(verbose_name=("Sacco Name"),unique=True, max_length=100, blank=False)
    sacco_address = models.CharField(blank=False, max_length=200, help_text='P.O Box 357')
    sacco_phonenumber = models.CharField(verbose_name=("Tel"), max_length=12)
    sacco_url = models.CharField(verbose_name=("Website"), max_length=250, default='')
    town = models.CharField(max_length=10, choices=LOCATION_CHOICES, default=0,blank=True,null=True)
    city = models.CharField(max_length=100, default='', blank=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.sacco_name

    class Meta:
        verbose_name_plural = 'Sacco profile Details'


# The table containing the details of owner of the matatu sacco

# This is a table that contains the details of the drivers employed to work for a respective matatu sacco

class DriverProfile(models.Model):

    STATUS_CHOICES = (
        ('Employed', 'Employed'),
        ('Dismissed', 'Dismissed'),
        ('Resigned', 'Resigned'),
        ('Left', 'Left'),
    )


    EMPLOYER_CHOICES = (
        ('AVARAGE DRIVER', 'Avarage driver'),
        ('GOOD DRIVER', 'Good driver'),
        ('VERY GOOD', 'Very Good'),
        ('WORST DRIVER', 'Worst driver'),
    )
    user_owner = models.ForeignKey(Saccoowner,verbose_name='Driver',on_delete=models.CASCADE,related_name='driverprofiles',null=False,default=1,unique=False)
    f_name = models.CharField(verbose_name=("First Name"),max_length=30, blank=True)
    l_name = models.CharField(verbose_name=("Last Name"),max_length=50, blank=True)
    dl = models.CharField(verbose_name=("Driving Licence"),max_length=8, default='',unique=True, blank=False)
    phone = models.CharField(max_length=20, blank=True, default='')
    route = models.CharField(max_length=100, default='', blank=False)
    employer=models.ForeignKey(SaccoProfile,on_delete=models.CASCADE,default=1)
    #driver_employer = models.ForeignKey(SaccoProfile,verbose_name=("employer"),default=1,on_delete=models.CASCADE,related_name='driversdetails')
    image = models.FileField(verbose_name=("Profile Picture"),upload_to='media', max_length=255, null=True, blank=True,default='')
    emp_rmks = models.CharField(verbose_name=("Employer Remarks"),max_length=100,choices=EMPLOYER_CHOICES,default='Good driver')
    driver_status=models.CharField(max_length=100, choices=STATUS_CHOICES,default='Employed')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = ' Sacco Driver Details'

# This is a table that contains the staff member details of a give matatu sacco.

class StaffProfile(models.Model):
    GENDER_CHOICES = (
        ('B', '--------'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Staff', on_delete=models.CASCADE, null=True)
    employer = models.ForeignKey(SaccoProfile,on_delete=models.CASCADE,null=True,default=False,related_name='staffprofiles')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='')
    picture = models.FileField(upload_to='media', blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    last_modified = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
           return self.user.first_name

    class Meta:
        verbose_name_plural = 'Sacco Staff Profiles'


#signals

"""
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    print('****', created)
    if instance.is_saccoowner:
        Saccoowner.objects.get_or_create(user=instance)
    elif instance.is_saccodriver:
        DriverProfile.objects.get_or_create(user=instance)
    else:
        StaffProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('_-----')
    # print(instance.internprofile.bio, instance.internprofile.location)
    if instance.is_saccoowner:
        instance.saccoowners.save()

    elif instance.is_saccodriver:
        instance.driver_profile.save()

    else:
        StaffProfile.objects.get_or_create(user=instance)

"""

