from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from ..models import DriverProfile

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_driver:
            return redirect('home')
        else:
            return redirect('search')
    return render(request, 'msacco/home.html')


def search(request):

    return render(request, 'msacco/search.html',)

def getProfile(request):
     error = []
     if 'q' in request.GET:
         q = request.GET['q']
         if not q:
             error.append('Enter a serach term.')
         elif len(q)> 9:
             error.append('Please Enter 8 characters.')
         else:
             profile = DriverProfile.objects.filter(dl__icontains=q)
             return render(request,'msacco/profResults.html',{'profile': profile, 'query': q})

     return render(request,'msacco/search.html', {'error': error})

