from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(extra_context = {'site_path': 'signup'}), name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html', extra_context = {'site_path': 'login'}), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
]