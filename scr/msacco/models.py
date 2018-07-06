from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

#model to create Employer profile
class EmployerProfile(models.Model):

    LOCATION_CHOICES = (
        ('None', "None"),
        ('Kasarani', "Kasarani"),
        ('Kawangware', "Kawangware"),
        ('Uthiru', "Uthiru"),
        ('Pipeline', "Pipeline"),
        ('Ngong', "Ngong"),
        ('Dohnholm', "Dohnholm"),
        ('Kilimani', "Kilimani"),
    )
    location = models.CharField(max_length=10,choices=LOCATION_CHOICES,default=0)
    orgName = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=False)

    def __str__(self):
        return self.orgName

#employer model
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile = models.ForeignKey(EmployerProfile,on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.user.username

# model to create driver profile
class DriverProfile(models.Model):
    fname = models.CharField(max_length=250,default='')
    sname = models.CharField(max_length=250,default='')
    email = models.EmailField(unique=True,default='')
    image = models.FileField(verbose_name=("Profile Picture"),upload_to='media', max_length=255, null=True, blank=True,default='')
    dl = models.CharField(verbose_name=("Driving Licence"),max_length=100, default='', blank=False)
    phone = models.CharField(max_length=20, blank=True, default='')
    route = models.CharField(max_length=100, default='', blank=False)
    employer = models.ForeignKey(EmployerProfile,on_delete=models.CASCADE,default=True)
    emp_rmks = models.TextField(verbose_name=("Employer Remarks"),max_length=100,blank=False,default='')