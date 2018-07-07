from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..models import User, DriverProfile
from ..forms import EmployerSignUpForm


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
        return redirect('deriverlist')


#Methods  >> list,create,save,edit,update,remove

"""employer.deriverlist"""
def driverlist(request):
   drivers = DriverProfile.objects.all()
   if not drivers:
        found = len(drivers)>0
   else:
        found = False
   return render(request, 'employer/driverlist.html', {'found' : found, 'drivers' : drivers})


def drivercreate(request):
   return render(request, 'employer/drivercreate.html')
