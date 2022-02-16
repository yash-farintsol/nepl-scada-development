from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name="dashboard-page"),
    path('', views.user_login, name="login-page"),
    path('login', views.user_login, name="login-page"),
    path('psw_change', views.pswd_change, name="User Password Change Page"),
    path('register', views.register, name="User Creation Page"),

    #path('SMSsettings', views.smsset, name="SMS Settings Page"),
    #path('Emailsettings', views.mailset, name="Mail Settings Page"),
    path('group_security', views.group_secur, name="Group Security Page"),
    path('user_security', views.user_secur, name="User Security Page"),
    #path('master_settings', views.master_set, name="Master Password Settings Page"),
    #path('database_settings', views.database_set, name="Database Settings Page"),
    path('sms-setting/', views.SMSSetting, name="sms-setting"),
    path('email-setting/', views.EmailSetting, name="email-setting"),
    path('database-setting/', views.DBSetting, name="database-setting"),
    path('master-password-setting/', views.MPSetting, name="master-password-setting"),
    path('general-setting/', views.GeneralSetting, name="general-setting"),

    path('create_equipment', views.equip_create, name="Equipment Creation"),
    path('eqp_parameter', views.eqp_param, name='Equipment Parameter'),
    path('eqp_activation', views.eqp_activ, name='Equipment Activation Page'),
    path('samp/', views.Samp, name="samp"),
    path('user-audit/', views.AuditUser, name="user-audit"),
    path('alarm-audit/', views.AuditAlarm, name="alarm-audit"),
    path('sms-audit/', views.AuditSMS, name="sms-audit"),
    path('equip-audit/', views.AuditEquip, name="equip-audit"),
    path('email-audit/', views.AuditEmail, name="email-audit"),
    path('template/', views.MSTemplate, name="template"),
    path('master-template/', views.MasterTemplate, name="master-template"),
    path('synchronize-date-time/', views.SyncDateTime, name="synchronize-date-time"),
    path('reset-lux-uv/', views.ResetLuxUV, name="reset-lux-uv"),
    path('io-status/', views.IOStatus, name="io-status"),
    path('graph-setting/', views.GraphSetting, name="graph-setting"),
    path('user-update-data/<str:pk>/', views.UserUpdateData, name="user-update-data"),



]