from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('register/success/', v.success, name='success'),
    path('register/', v.register, name='register'),
    # path('register/success', v.)


]
