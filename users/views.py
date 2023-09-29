from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from .models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView

class UsersListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('stocks:index')

class CustomRegistrationView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class CustomLogoutView(LogoutView):
    template_name = 'users/login.html'