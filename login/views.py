from django.shortcuts import render, redirect 
from .forms import RegistrationForm
from django.contrib.auth import login as login_user
from django.contrib.auth.decorators import login_required 

@login_required
def login(request):
    return render(request, 'main/base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_user(request, user)
            return redirect('/')
        
    else: form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

