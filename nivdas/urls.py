from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name="dashboard-page"),
    path('', views.user_login, name="login-page"),
    path('login', views.user_login, name="login-page"),
    path('psw_change', views.pswd_change, name="User Password Change Page"),
    path('register', views.register, name="User Creation Page"),
    path('SMSsettings', views.smsset, name="SMS Settings Page"),
    path('Emailsettings', views.mailset, name="Mail Settings Page"),
    path('group_security', views.group_secur, name="Group Security Page"),
    path('user_security', views.user_secur, name="User Security Page"),
    path('master_settings', views.master_set, name="Master Password Settings Page"),
    path('database_settings', views.database_set, name="Database Settings Page"),



]