<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from carticle.models import Article

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

@login_required
def dashboard(request):
    article = Article.objects.all()
    data = {}
    data['object_list'] = article
    return render(request, 'accounts/dashboard.html',data)

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

>>>>>>> bdda1b0f1608ddf5170c5b27a275bf6e3e3e1b48
