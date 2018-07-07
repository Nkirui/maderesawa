from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from ..models import DriverProfile

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_driver:
            return redirect('search')
        else:
            return redirect('driverlist')
    return render(request, 'msacco/home.html')



