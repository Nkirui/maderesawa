from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render, get_object_or_404

from ..models import DriverProfile, Saccoowner,SaccoProfile,User
from ..forms import SaccoOwnerSignUpForm, DriverForm, OwnerProfileForm, SaccoProfileForm, StaffProfileForm


def EmployerSignUpView(request):

    if request.method == 'POST':

        owner_form = SaccoOwnerSignUpForm(request.POST)
        ownerProf_form = OwnerProfileForm(request.POST)
        saccoprof = SaccoProfileForm(request.POST)


        if owner_form.is_valid() and ownerProf_form.is_valid() and saccoprof.is_valid() :


                user = owner_form.save(commit=False)
                user.save()

                profile = ownerProf_form.save(commit=False)
                profile.user = user
                profile.save()

                sacco_prof = saccoprof.save(commit=False)
                sacco_prof.owner=profile
                sacco_prof.save()



                return redirect('driverlist')

    else:
        owner_form = SaccoOwnerSignUpForm()
        ownerProf_form = OwnerProfileForm()
        saccoprof=SaccoProfileForm()




    return render(request, 'registration/signup_form.html', {
        'owner_form': owner_form,
        'ownerProf_form': ownerProf_form,
        'saccoprof':saccoprof

    })

#Methods  >> list,create,save,edit,update,remove

"""employer.deriverlist """
@login_required()
def driverlist(request):

   x = SaccoProfile.objects.get(owner__user__username=request.user)
   drivers=DriverProfile.objects.all().filter(employer__sacco_name=x.sacco_name)

   if not drivers:
        found = len(drivers)>0
   else:
        found = False
       
   return render(request, 'employer/driverlist.html', {'found' : found, 'drivers' : drivers})


def drivercreate(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():

        driver = form.save(commit=False)
        x = SaccoProfile.objects.get(owner__user__username=request.user)
        employer = SaccoProfile.objects.get(sacco_name=x.sacco_name)
        employer.save()
        driver.employer=employer
        driver.save()

        return redirect('driverlist')
    return render(request, 'employer/drivercreate.html', {'form': form})


def driverview(request, pk):

    driver= DriverProfile.objects.get(pk=pk)
            #get_object_or_404(DriverProfile, pk=pk)
    return render(request, 'employer/driverdetails.html', {'object':driver})

def driveredit(request, pk):
    driver= get_object_or_404(DriverProfile, pk=pk)
    form = DriverForm(request.POST or None,instance=driver)
    if form.is_valid():
        form.save()
        return redirect('driverlist')

    return render(request, 'employer/drivercreate.html', {'form':form})

def driverremove(request,pk):
    driver=get_object_or_404(DriverProfile, pk=pk)

    if request.method == 'POST':
        driver.delete()
        return redirect('driverlist')


    return render(request, 'employer/driverconfirmdelete.html',{'driver':driver})

# display the profile information

def saccoprofdisp(request):
  prof = SaccoProfile.objects.get(owner__user__username=request.user)
 # prof = SaccoProfile.objects.all().filter(sacco_name=x.sacco_name)
  return render(request,'employer/companyprofiledata.html',{'prof': prof})

def createstaff(request):
    if request.method == 'POST':
        staff_form = StaffProfileForm(request.POST)
        if staff_form.is_valid():
            user = staff_form.save(commit=False)
            user.save()

            return redirect('driverlist')

    else:
        staff_form = StaffProfileForm()

    return render(request, 'employer/staffcreate.html', {'staff_form': staff_form,})







