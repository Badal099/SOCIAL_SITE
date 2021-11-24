from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from Account.forms import RegistrationForm

# Create your views here.


def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('userlogin')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'register.html', context)


def userlogin(request):
    error = ""
    if request.method == 'POST':
        contact = request.POST['contact']
        password = request.POST['password']
        user = authenticate(contact=contact, password=password)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'userlogin.html', d)
