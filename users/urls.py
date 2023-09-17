from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
]