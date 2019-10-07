from django.urls import path, include
from .views import home, create_view, profile_view, null_view

urlpatterns = [
    path('', null_view),
    path('home/', home, name='home'),
    path('create/', create_view, name='create'),
    path('profile/', profile_view, name='profile'),
]
