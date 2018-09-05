from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from ..models import DriverProfile

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_saccoowner:
            return redirect('driverlist')
        elif request.user.is_saccostaff:
            return redirect('staffaccount')
        else:
            return redirect('search')
    return render(request, 'msacco/home.html')



