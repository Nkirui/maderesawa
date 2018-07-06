from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from ..forms import DriverSignUpForm
from ..models import User, DriverProfile


class DriverSignUpView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'driver'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('search')


# crude operation methods
def list(request):
   drivers = DriverProfile.objects.all()
   if not drivers:
        found = len(drivers)>0
   else:
        found = False
   return render(request, 'driver/list.html', {'found' : found, 'drivers' : drivers})

