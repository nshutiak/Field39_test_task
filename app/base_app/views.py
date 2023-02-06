from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .models import Userdata
from .decorators import check_form_accessibility
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    logout(request)
    '''
    functions for login/logout
    '''
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    return render(request, 'authorization/login.html')


decorators = [
    login_required(login_url='authorization/'), check_form_accessibility
]


@method_decorator(decorators, name='dispatch')
class CreateFormView(CreateView):
    '''
    Form creator class (POST), accept data from html form
    '''
    model = Userdata
    fields = ('username', 'password', 'email', 'phone_number')
    success_url = "/"
    template_name = "form/form.html"


class UserdataListView(ListView):
    '''
    Returning the list of all users data
    '''
    model = Userdata
    template_name = "form/test.html"