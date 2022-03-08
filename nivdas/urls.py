from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path("",views.LoginPage,name="loginpage"),
    path("dashboard/",views.IndexPage,name="indexpage"),
    path("user-management/",views.RegisterPage,name="user-management"),
    path("group-security/",views.GroupSec,name="groupsec"),
    path("user-update/",views.UpdateUserData,name="user-update"),
    path("database-setting/",views.DatabaseSettingPage,name="DatabaseSettingPage"),
    path("create-equip/",views.CreateEquipment,name="equipment"),
    path("login/",views.Login,name="login"),
    path("Add-user/",views.AddUser,name="AddUser"),
    path("store-sms-setting/",views.StoreSmsSetting,name="storesms"),
    path("store-email-setting/",views.StoreEmailSetting,name="storeemail"),
    path("update-master-password-setting/",views.MasterPasswordSetting,name="masterpasswdsetting"),
    path('user-update-data/<str:pk>/', views.UserUpdateData, name="user-update-data"),
    path("store-database-setting/",views.StoreDatabaseSetting,name="StoreDatabaseSetting"),
    path('group-security-data/<str:pk>/', views.GroupSecurityData, name="group-security-data"),
    path('user-security-data/<str:pk>/', views.UserSecurityData, name="user-security-data"),
    path("user-security/",views.UserSec,name="usersec"),
    path('assign-group-security/',views.AssignGroupSecurity,name="assign-group-security"),
    path('assign-user-security/',views.AssignUserSecurity,name="assign-user-security"),
    path('sms-setting/', views.SMSsettings, name="sms-setting"),
    path('email-setting/', views.EmailSettings, name="email-setting"),
    path('master-password-setting/', views.MPSetting, name="master-password-setting"),
    path('general-setting/', views.GeneralSetting, name="general-setting"),
    path('equipment-creation', views.EquipmentCreation, name="equipment-creation"),
    path('equipment-parameter', views.EquipmentParameter, name="equipment-parameter"),
    path('equipment-activation', views.EquipmentActivation, name="equipment-activation"),
    path('template/', views.MSTemplate, name="template"),
    path('store-template-settings/',views.StoreTemplate,name="store_mail_template"),
    path('mobile-number/', views.MobileNo, name="mobile-number"),
    path('master-template/', views.MasterTemplate, name="master-template"),
    path('synchronize-date-time/', views.SyncDateTime, name="synchronize-date-time"),
    path('reset-lux-uv/', views.ResetLuxUV, name="reset-lux-uv"),
    path('io-status/', views.IOStatus, name="io-status"),
    path('data-view/', views.DataView, name="data-view"),
    path('luxuv-data-view/', views.LuxUVDataView, name="luxuv-data-view"),
    path('user-audit/', views.AuditUser, name="user-audit"),
    path('alarm-audit/', views.AuditAlarm, name="alarm-audit"),
    path('sms-audit/', views.AuditSMS, name="sms-audit"),
    path('equipment-audit/', views.AuditEquip, name="equipment-audit"),
    path('email-audit/', views.AuditEmail, name="email-audit"),
    path('user-audit-history/', views.HistoryAuditUser, name="user-audit-history"),
    path('alarm-audit-history/', views.HistoryAuditAlarm, name="alarm-audit-history"),
    path('sms-audit-history/', views.HistoryAuditSMS, name="sms-audit-history"),
    path('equipment-audit-history/', views.HistoryAuditEquip, name="equipment-audit-history"),
    path('email-audit-history/', views.HistoryAuditEmail, name="email-audit-history"),
    path('data-view-history/', views.HistoryDataView, name="data-view-history"),
    path('luxuv-data-view-history/', views.HistoryLuxUVDataView, name="luxuv-data-view-history"),
    path('graph-setting/', views.GraphSetting, name="graph-setting"),
    path('password-setting/', views.PasswordSetting, name="password-setting"),
    path('print-multiple-reports/', views.PrintMultipleReports, name="print-multiple-reports"),
    path('about-us/', views.AboutUs, name="about-us"),
    path('equipment-list/', views.EquipmentList, name="equipment-list"),
    path('report-approval/', views.ReportApproval, name="report-approval"),
    path('status-report/', views.StatusReport, name="status-report"),
    path('equipment-parameter-data/<str:pk>/', views.EquipParamUpdateData, name="equipment-parameter-data"),
    path('graph1/', views.Graph1, name="graph1"),
    path('graph2/', views.Graph2, name="graph2"),
    path('pdf/', views.GeneratePdf,name="pdf"),
    path('samp/',views.samp,name="samp"),
    path("verify-admin/", views.VerifyUser, name="verify-admin"),
]