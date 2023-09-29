from django.urls import path
from . import views
from .views import CustomLoginView, CustomRegistrationView, LogoutView

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]