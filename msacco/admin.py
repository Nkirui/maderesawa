from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from msacco.forms import StaffSignupForm
from .models import SaccoProfile, DriverProfile, StaffProfile, User, Saccoowner


# register Emplolyerprofile

class SaccoOwnerProfileAdmin(admin.ModelAdmin):

    list_display = ['sacco_name','owner','sacco_address','sacco_phonenumber','sacco_url','town','city','created_on']

admin.site.register(SaccoProfile,SaccoOwnerProfileAdmin)


#register Driverprofile
class DriverProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = DriverProfile

    search_fields = ('image','dl','phone','route' )
    list_display = ['employer','f_name','l_name','image', 'dl','phone','route','emp_rmks','created_on']
    fields = ['employer','f_name','l_name','image', 'dl','phone','route','emp_rmks']
    list_filter = ('employer',)

admin.site.register(DriverProfile, DriverProfileAdmin)

# staff profile


class StaffProfileAdmin(admin.ModelAdmin):

    model = StaffProfile

    list_display = ['user','gender','picture','employer','created_on']
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)
    list_filter = ('employer',)



admin.site.register(StaffProfile, StaffProfileAdmin)


# admin.site.register(User,UserAdmin )
# usercreation forms


class UserAdmin(BaseUserAdmin):

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','email','username','password1', 'password2')}
        ),
    )
admin.site.register(User, UserAdmin)


# owners of the sacco Adminprofile
class SaccoOwnerAdmin(admin.ModelAdmin):

    model = Saccoowner
    list_display = ('user','national_id','phone_number','address','created_on')
    date_hierarchy = 'created_on'
    ordering = ('-created_on',)
    fields = ('user', 'national_id','phone_number','address')



admin.site.register(Saccoowner, SaccoOwnerAdmin)

admin.site.site_header = 'Madere Sacco Administration',