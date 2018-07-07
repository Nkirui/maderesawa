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


def search(request):

    return render(request, 'driver/search.html',)


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

