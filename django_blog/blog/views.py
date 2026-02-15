

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in user
            return redirect("profile")
    else:
        form = CustomUserRegistrationForm()

    return render(request, "users/register.html", {"form": form})

def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "users/profile.html", {"form": form})