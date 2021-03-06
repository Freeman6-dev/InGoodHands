"""InGoodHands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from charity_donation_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('add_donation/', views.AddDonationView.as_view(), name='add_donation'),
    path('remind_password/', views.RemindPasswordView.as_view(), name='remind_password'),
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('user_profile/taken/<int:pk>', views.DonationTakenView.as_view(), name='taken'),
    path('settings/', views.UserSettingsView.as_view(), name='user_settings'),
    path('settings/change_password/', views.ChangeUserPasswordView.as_view(), name='change_password'),


]
