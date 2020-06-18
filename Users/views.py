from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def register(request):
    if request.method=="POST":
        #django provides forms
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You can login now')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'Users/Signup.html', {'form':form})

def profile(request):
    l = []
    all_users = get_user_model().objects.all()
    for i in all_users:
        print(i)
    context = {'all': all_users}
    print(context)
    print(all)
    return render(request, 'Users/profile.html', context)