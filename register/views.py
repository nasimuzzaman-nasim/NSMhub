from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm


def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('success/')

    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


def success(response):
    return render(response, "register/success.html", {})


# def logout_view(request):
#     # logout(request)
#     return render(request, 'registration/logout.html', {})
