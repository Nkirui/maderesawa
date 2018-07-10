from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView

from ..models import User, DriverProfile
from ..forms import EmployerSignUpForm, DriverForm


class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('driverlist')


#Methods  >> list,create,save,edit,update,remove

"""employer.deriverlist """
def driverlist(request):
   drivers = DriverProfile.objects.all()
   if not drivers:
        found = len(drivers)>0
   else:
        found = False
       
   return render(request, 'employer/driverlist.html', {'found' : found, 'drivers' : drivers})

def drivercreate(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('driverlist')
    return render(request, 'employer/drivercreate.html', {'form': form})


def driverview(request, pk):
    driver= get_object_or_404(DriverProfile, pk=pk)
    return render(request, 'employer/driverdetails.html', {'object':driver})

def driveredit(request, pk):
    driver= get_object_or_404(DriverProfile, pk=pk)
    form = DriverForm(request.POST or None,instance=driver)
    if form.is_valid():
        form.save()
        return redirect('driverlist')

    return render(request, 'employer/drivercreate.html', {'form':form})

def driverremove(request, pk):
    driver= get_object_or_404(DriverProfile, pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('driverlist')
    return render(request, 'employer/driverconfirmdelete.html',{'driver':driver})