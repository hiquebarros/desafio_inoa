from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from .models import User
from django.urls import reverse_lazy

class UsersListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('stocks:index')