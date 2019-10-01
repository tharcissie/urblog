from .forms import *
from carticle.models import Article
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required






#####################     function for rendering signup form on page    ######################

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

#####################     function for rendering the dashboard page   ######################

@login_required
def dashboard(request):
    article = Article.objects.all()
    data = {}
    data['object_list'] = article
    return render(request, 'accounts/dashboard.html',data)

#####################     function for updating user profile inforamtion and profile picture     ######################

@login_required
def update_profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid():
            u_form.save()
            p_form.save()
      
            return redirect('update_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/update_profile.html',{'u_form':u_form, 'p_form':p_form})

