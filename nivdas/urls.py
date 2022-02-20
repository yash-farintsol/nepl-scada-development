from django.urls import path
from . import views

urlpatterns = [
    path("",views.LoginPage,name="loginpage"),
    path("dashboard/",views.IndexPage,name="indexpage"),
    path("user-management/",views.RegisterPage,name="user-management"),
    path("group-security/",views.GroupSec,name="groupsec"),
    path("database-setting/",views.DatabaseSettingPage,name="DatabaseSettingPage"),
    path("login/",views.Login,name="login"),
    path("Add-user/",views.AddUser,name="AddUser"),
    path('user-update-data/<str:pk>/', views.UserUpdateData, name="user-update-data"),
    path("store-database-setting/",views.StoreDatabaseSetting,name="StoreDatabaseSetting"),
]