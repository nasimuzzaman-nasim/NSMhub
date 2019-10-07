from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import BlogForm
from .models import Blog


def null_view(response):
    return render(response, 'null.html', {})


def base_view(response):
    return render(response, 'afterloginBase.html', {})


def home(response):
    # if user
    return render(response, 'home.html', {})


def create_view(response):
    if response.method == 'POST':
        form = BlogForm(response.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = response.user.username
            new_form.save()
        # if form.is_valid():
        #     form.save()

        return redirect('../profile/')
    else:
        form = BlogForm()
    return render(response, 'createPost.html', {'form': form})


def profile_view(response):
    queryset = Blog.objects.all().order_by('-time')
    return render(response, 'profile.html', {'qs': queryset})