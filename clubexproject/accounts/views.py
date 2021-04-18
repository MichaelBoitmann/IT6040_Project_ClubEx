from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm

def registration_view(request):
    context={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username,password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/signup.html', context)
