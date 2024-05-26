from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

from .forms import UserRegisterForm
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  # Bind data to the form
        if form.is_valid():
            form.save()  # Save the form to create a new user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username} .Log in Now!!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})