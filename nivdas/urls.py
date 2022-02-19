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
    path('group-security-data/<str:pk>/', views.GroupSecurityData, name="group-security-data"),
    path('user-security-data/<str:pk>/', views.UserSecurityData, name="user-security-data"),
    path("user-security/",views.UserSec,name="usersec"),
    path('assign-group-security/',views.AssignGroupSecurity,name="assign-group-security"),
    path('assign-user-security/',views.AssignUserSecurity,name="assign-user-security"),
]