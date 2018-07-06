from django.contrib import admin

# Register your models here.
from .models import Driver, Employer, EmployerProfile, DriverProfile

admin.site.register(Driver)

class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('location', 'orgName', 'city')

admin.site.register(EmployerProfile,EmployerProfileAdmin)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('profile',)

admin.site.register(Employer,EmployerAdmin)

class DriverProfileAdmin(admin.ModelAdmin):
    search_fields = (
    'image',
    'dl',
    'phone',
    'route'
    )

    list_display = ['fname','sname','image', 'dl','phone','route','employer','emp_rmks']

admin.site.register(DriverProfile, DriverProfileAdmin)