from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

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
        context = {'name': all_users}

    print(context)
    return render(request, 'Users/profile.html', context)

def delete(request):
    print("Welcome")
    print(request.POST.get('all_users'))
    user_id = request.POST.get('all_users')
    print(user_id)
    obj = get_object_or_404(User, username=user_id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, f'"{user_id}" is deleted successfully')
        return redirect("/accounts/profile/")
