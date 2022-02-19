from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
import ast
from django.http import JsonResponse


def LoginPage(request):
    return render(request, "nivdas/login.html")


def IndexPage(request):
    if 'username' in request.session:
        return render(request, "nivdas/index.html")
    else:
        return redirect("loginpage")

def RegisterPage(request):
    if 'username' in request.session:
        GetGroups = Group.objects.all()
        AllUsers = User.objects.all()
        return render(request, "nivdas/register.html",{'groups':GetGroups,'alluser':AllUsers})
    else:
        return redirect("loginpage")

def GroupSec(request):
    if 'username' in request.session:
        groups = Group.objects.all()
        return render(request, "nivdas/group_sec.html", {'group': groups})
    else:
        return redirect("loginpage")

def DatabaseSettingPage(request):
    if 'username' in request.session:
        return render(request, "nivdas/db-setting.html")
    else:
        return redirect("loginpage")

def Login(request):
    print("HELLO")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        usr = User.objects.filter(Username=username)

        if len(usr) > 0:
            if usr[0].Password == password:
                request.session['username'] = usr[0].Username
                get_user_security = UserSecurity.objects.filter(User=usr[0])
                get_group_security = GroupSecurity.objects.filter(Group=usr[0].Group)
                
                if len(get_user_security) > 0:
                    request.session['UserCreation'] = get_user_security[0].UserCreation
                    request.session['GroupSec'] = get_user_security[0].GroupSec
                    request.session['UserSec'] = get_user_security[0].UserSec
                    request.session['DatabaseSetting'] = get_user_security[0].DatabaseSetting
                    request.session['SMSsetting'] = get_user_security[0].SMSsetting
                    request.session['EmailSetting'] = get_user_security[0].EmailSetting
                    request.session['MasterPasswdSetting'] = get_user_security[0].MasterPasswdSetting
                    request.session['GeneralSetting'] = get_user_security[0].GeneralSetting
                    request.session['EquipmentCreation'] = get_user_security[0].EquipmentCreation
                    request.session['EquipmentParameter'] = get_user_security[0].EquipmentParameter
                    request.session['EquipmentActivation'] = get_user_security[0].EquipmentActivation
                    request.session['Template'] = get_user_security[0].Template
                    request.session['MobileNumber'] = get_user_security[0].MobileNumber
                    request.session['MasterTemplate'] = get_user_security[0].MasterTemplate
                    request.session['SyncDataTime'] = get_user_security[0].SyncDataTime
                    request.session['ResetLuxUV'] = get_user_security[0].ResetLuxUV
                    request.session['InputOutputStatus'] = get_user_security[0].InputOutputStatus
                    request.session['EquipmentList'] = get_user_security[0].EquipmentList
                    request.session['DataView'] = get_user_security[0].DataView
                    request.session['LuxUVDataView'] = get_user_security[0].LuxUVDataView
                    request.session['ReportApproval'] = get_user_security[0].ReportApproval
                    request.session['StatusReports'] = get_user_security[0].StatusReports
                    request.session['UserAudit'] = get_user_security[0].UserAudit
                    request.session['AlarmAudit'] = get_user_security[0].AlarmAudit
                    request.session['SMSAudit'] = get_user_security[0].SMSAudit
                    request.session['EquipmentAudit'] = get_user_security[0].EquipmentAudit
                    request.session['EmailAudit'] = get_user_security[0].EmailAudit
                    request.session['DataReportGraph'] = get_user_security[0].DataReportGraph
                    request.session['LuxUVDataView'] = get_user_security[0].LuxUVDataView
                    request.session['HUserAudit'] = get_user_security[0].HUserAudit
                    request.session['HAlarmAudit'] = get_user_security[0].HAlarmAudit
                    request.session['HSMSAudit'] = get_user_security[0].HSMSAudit
                    request.session['HEquipmentAudit'] = get_user_security[0].HEquipmentAudit
                    request.session['HEmailAudit'] = get_user_security[0].HEmailAudit
                    request.session['GraphSettings'] = get_user_security[0].GraphSettings
                    request.session['PasswordSettings'] = get_user_security[0].PasswordSettings
                    request.session['PrintMultipleReports'] = get_user_security[0].PrintMultipleReports
                    request.session['AboutUs'] = get_user_security[0].AboutUs
                    request.session['Help'] = get_user_security[0].Help
                else:
                    request.session['UserCreation'] = get_group_security[0].UserCreation
                    request.session['GroupSec'] = get_group_security[0].GroupSec
                    request.session['UserSec'] = get_group_security[0].UserSec
                    request.session['DatabaseSetting'] = get_group_security[0].DatabaseSetting
                    request.session['SMSsetting'] = get_group_security[0].SMSsetting
                    request.session['EmailSetting'] = get_group_security[0].EmailSetting
                    request.session['MasterPasswdSetting'] = get_group_security[0].MasterPasswdSetting
                    request.session['GeneralSetting'] = get_group_security[0].GeneralSetting
                    request.session['EquipmentCreation'] = get_group_security[0].EquipmentCreation
                    request.session['EquipmentParameter'] = get_group_security[0].EquipmentParameter
                    request.session['EquipmentActivation'] = get_group_security[0].EquipmentActivation
                    request.session['Template'] = get_group_security[0].Template
                    request.session['MobileNumber'] = get_group_security[0].MobileNumber
                    request.session['MasterTemplate'] = get_group_security[0].MasterTemplate
                    request.session['SyncDataTime'] = get_group_security[0].SyncDataTime
                    request.session['ResetLuxUV'] = get_group_security[0].ResetLuxUV
                    request.session['InputOutputStatus'] = get_group_security[0].InputOutputStatus
                    request.session['EquipmentList'] = get_group_security[0].EquipmentList
                    request.session['DataView'] = get_group_security[0].DataView
                    request.session['LuxUVDataView'] = get_group_security[0].LuxUVDataView
                    request.session['ReportApproval'] = get_group_security[0].ReportApproval
                    request.session['StatusReports'] = get_group_security[0].StatusReports
                    request.session['UserAudit'] = get_group_security[0].UserAudit
                    request.session['AlarmAudit'] = get_group_security[0].AlarmAudit
                    request.session['SMSAudit'] = get_group_security[0].SMSAudit
                    request.session['EquipmentAudit'] = get_group_security[0].EquipmentAudit
                    request.session['EmailAudit'] = get_group_security[0].EmailAudit
                    request.session['DataReportGraph'] = get_group_security[0].DataReportGraph
                    request.session['LuxUVDataView'] = get_group_security[0].LuxUVDataView
                    request.session['HUserAudit'] = get_group_security[0].HUserAudit
                    request.session['HAlarmAudit'] = get_group_security[0].HAlarmAudit
                    request.session['HSMSAudit'] = get_group_security[0].HSMSAudit
                    request.session['HEquipmentAudit'] = get_group_security[0].HEquipmentAudit
                    request.session['HEmailAudit'] = get_group_security[0].HEmailAudit
                    request.session['GraphSettings'] = get_group_security[0].GraphSettings
                    request.session['PasswordSettings'] = get_group_security[0].PasswordSettings
                    request.session['PrintMultipleReports'] = get_group_security[0].PrintMultipleReports
                    request.session['AboutUs'] = get_group_security[0].AboutUs
                    request.session['Help'] = get_group_security[0].Help

                return redirect("indexpage")
            else:
                print("Password is incorrect")
                return redirect("loginpage")
        else:
            print("User Doesn't Exist")
            return redirect("loginpage")


def AddUser(request):
    if request.method == "POST":
        username = request.POST['username']
        group = request.POST['group']
        department = request.POST['department']
        status = request.POST['status']
        password = request.POST['password']
        PasswordChangeDuration = request.POST['PasswdChangeDuration']
        
        GetGroup = Group.objects.get(GroupName=group)
        print("ADD GORUP TO USER-->",GetGroup)
        usr = User.objects.create(Username=username,
        Password=password,PasswdChangeDuration=PasswordChangeDuration,
        Department=department,status=status)
        usr.Group = GetGroup
        usr.save()
        return redirect("user-management")

def UserUpdateData(request, pk):
    print(pk)
    getann = User.objects.get(Username=pk)
    print(getann)
    data = []
    item = {
        'name': getann.Username,
        'password': getann.Password,
        'grp_name': getann.Group.GroupName,
        'dep_name': getann.Department,
        'status': getann.status,
        'cpassword': getann.PasswdChangeDuration
    }
    data.append(item)
    return JsonResponse({'data': data})

def GroupSecurityData(request, pk):
    print(pk)
    GetGroup = Group.objects.get(GroupName=pk)
    get_security = GroupSecurity.objects.get(Group=GetGroup)
    print(get_security)
    item = {
        'userCreation': get_security.UserCreation,
        'groupSec': get_security.GroupSec,
        'userSec': get_security.UserSec,
        'databaseSetting': get_security.DatabaseSetting,
        'SMSSetting': get_security.SMSsetting,
        'emailSetting': get_security.EmailSetting,
        'MasterPasswdSetting': get_security.MasterPasswdSetting,
        'GeneralSetting': get_security.GeneralSetting,
        'EquipmentCreation': get_security.EquipmentCreation,
        'EquipmentParameter': get_security.EquipmentParameter,
        'EquipmentActivation': get_security.EquipmentActivation,
        'Template': get_security.Template,
        'MobileNumber': get_security.MobileNumber,
        'MasterTemplate': get_security.MasterTemplate,
        'SyncDataTime': get_security.SyncDataTime,
        'ResetLuxUV': get_security.ResetLuxUV,
        'InputOutputStatus': get_security.InputOutputStatus,
        'EquipmentList': get_security.EquipmentList,
        'DataView': get_security.DataView,
        'LuxUVDataView': get_security.LuxUVDataView,
        'ReportApproval': get_security.ReportApproval,
        'StatusReports': get_security.StatusReports,
        'UserAudit': get_security.UserAudit,
        'AlarmAudit': get_security.AlarmAudit,
        'SMSAudit': get_security.SMSAudit,
        'EquipmentAudit': get_security.EquipmentAudit,
        'EmailAudit': get_security.EmailAudit,
        'DataReportGraph': get_security.DataReportGraph,
        'LuxUVDataView': get_security.LuxUVDataView,
        'HUserAudit': get_security.HUserAudit,
        'HAlarmAudit': get_security.HAlarmAudit,
        'HSMSAudit': get_security.HSMSAudit,
        'HEquipmentAudit': get_security.HEquipmentAudit,
        'HEmailAudit': get_security.HEmailAudit,
        'GraphSettings': get_security.GraphSettings,
        'PasswordSettings': get_security.PasswordSettings,
        'PrintMultipleReports': get_security.PrintMultipleReports,
        'AboutUs': get_security.AboutUs,
        'Help': get_security.Help
    }
    return JsonResponse({'data': item})

def UserSecurityData(request, pk):
    GetUser = User.objects.get(Username=pk)
    get_security = GroupSecurity.objects.get(Group=GetUser.Group)
    item = {
        'userCreation': get_security.UserCreation,
        'groupSec': get_security.GroupSec,
        'userSec': get_security.UserSec,
        'databaseSetting': get_security.DatabaseSetting,
        'SMSSetting': get_security.SMSsetting,
        'emailSetting': get_security.EmailSetting,
        'MasterPasswdSetting': get_security.MasterPasswdSetting,
        'GeneralSetting': get_security.GeneralSetting,
        'EquipmentCreation': get_security.EquipmentCreation,
        'EquipmentParameter': get_security.EquipmentParameter,
        'EquipmentActivation': get_security.EquipmentActivation,
        'Template': get_security.Template,
        'MobileNumber': get_security.MobileNumber,
        'MasterTemplate': get_security.MasterTemplate,
        'SyncDataTime': get_security.SyncDataTime,
        'ResetLuxUV': get_security.ResetLuxUV,
        'InputOutputStatus': get_security.InputOutputStatus,
        'EquipmentList': get_security.EquipmentList,
        'DataView': get_security.DataView,
        'LuxUVDataView': get_security.LuxUVDataView,
        'ReportApproval': get_security.ReportApproval,
        'StatusReports': get_security.StatusReports,
        'UserAudit': get_security.UserAudit,
        'AlarmAudit': get_security.AlarmAudit,
        'SMSAudit': get_security.SMSAudit,
        'EquipmentAudit': get_security.EquipmentAudit,
        'EmailAudit': get_security.EmailAudit,
        'DataReportGraph': get_security.DataReportGraph,
        'LuxUVDataView': get_security.LuxUVDataView,
        'HUserAudit': get_security.HUserAudit,
        'HAlarmAudit': get_security.HAlarmAudit,
        'HSMSAudit': get_security.HSMSAudit,
        'HEquipmentAudit': get_security.HEquipmentAudit,
        'HEmailAudit': get_security.HEmailAudit,
        'GraphSettings': get_security.GraphSettings,
        'PasswordSettings': get_security.PasswordSettings,
        'PrintMultipleReports': get_security.PrintMultipleReports,
        'AboutUs': get_security.AboutUs,
        'Help': get_security.Help
    }
    return JsonResponse({'data': item})

def UserSec(request):
    if 'username' in request.session:
        users = User.objects.all()
        return render(request, "nivdas/user_sec.html", {'user': users})
    else:
        return redirect("loginpage")

def AssignGroupSecurity(request):
    if request.method == "POST":
        getGroup = Group.objects.get(GroupName = request.POST['Group'])
        getSecurity = GroupSecurity.objects.get(Group=getGroup)
        admin = request.POST.getlist('Admin1')
        masterSetting = request.POST.getlist('Master1')
        supervise = request.POST.getlist('Supervise1')
        auditTrails = request.POST.getlist('Audit1')
        history = request.POST.getlist('History1')
        tools = request.POST.getlist('Tool1')
        help = request.POST.getlist('Help1')

        if "UserCreation" in admin:
            getSecurity.UserCreation = True
        else:
            getSecurity.UserCreation = False
        if "GroupSec" in admin:
            getSecurity.GroupSec = True
        else:
            getSecurity.GroupSec = False
        if "UserSec" in admin:
            getSecurity.UserSec = True
        else:
            getSecurity.UserSec = False
        if "DatabaseSetting" in admin:
            getSecurity.DatabaseSetting = True
        else:
            getSecurity.DatabaseSetting = False
        if "SMSsetting" in admin:
            getSecurity.SMSsetting = True
        else:
            getSecurity.SMSsetting = False
        if "EmailSetting" in admin:
            getSecurity.EmailSetting = True
        else:
            getSecurity.EmailSetting = False
        if "MasterPasswdSetting" in admin:
            getSecurity.MasterPasswdSetting = True
        else:
            getSecurity.MasterPasswdSetting = False
        if "GeneralSetting" in admin:
            getSecurity.GeneralSetting = True
        else:
            getSecurity.GeneralSetting = False
        
        if "EquipmentCreation" in masterSetting:
            getSecurity.EquipmentCreation = True
        else:
            getSecurity.EquipmentCreation = False
        if "EquipmentParameter" in masterSetting:
            getSecurity.EquipmentParameter = True
        else:
            getSecurity.EquipmentParameter = False
        if "EquipmentActivation" in masterSetting:
            getSecurity.EquipmentActivation = True
        else:
            getSecurity.EquipmentActivation = False
        if "Template" in masterSetting:
            getSecurity.Template = True
        else:
            getSecurity.Template = False
        if "MobileNumber" in masterSetting:
            getSecurity.MobileNumber = True
        else:
            getSecurity.MobileNumber = False
        if "MasterTemplate" in masterSetting:
            getSecurity.MasterTemplate = True
        else:
            getSecurity.MasterTemplate = False
        if "SyncDataTime" in masterSetting:
            getSecurity.SyncDataTime = True
        else:
            getSecurity.SyncDataTime = False
        if "ResetLuxUV" in masterSetting:
            getSecurity.ResetLuxUV = True
        else:
            getSecurity.ResetLuxUV = False
        if "InputOutputStatus" in masterSetting:
            getSecurity.InputOutputStatus = True
        else:
            getSecurity.InputOutputStatus = False
        
        if "EquipmentList" in supervise:
            getSecurity.EquipmentList = True
        else:
            getSecurity.EquipmentList = False
        if "DataView" in supervise:
            getSecurity.DataView = True
        else:
            getSecurity.DataView = False
        if "LuxUVDataView" in supervise:
            getSecurity.LuxUVDataView = True
        else:
            getSecurity.LuxUVDataView = False
        if "ReportApproval" in supervise:
            getSecurity.ReportApproval = True
        else:
            getSecurity.ReportApproval = False
        if "StatusReports" in supervise:
            getSecurity.StatusReports = True
        else:
            getSecurity.StatusReports = False
        
        if "UserAudit" in auditTrails:
            getSecurity.UserAudit = True
        else:
            getSecurity.UserAudit = False
        if "AlarmAudit" in auditTrails:
            getSecurity.AlarmAudit = True
        else:
            getSecurity.AlarmAudit = False
        if "SMSAudit" in auditTrails:
            getSecurity.SMSAudit = True
        else:
            getSecurity.SMSAudit = False
        if "EquipmentAudit" in auditTrails:
            getSecurity.EquipmentAudit = True
        else:
            getSecurity.EquipmentAudit = False
        if "EmailAudit" in auditTrails:
            getSecurity.EmailAudit = True
        else:
            getSecurity.EmailAudit = False
        
        if "DataReportGraph" in history:
            getSecurity.DataReportGraph = True
        else:
            getSecurity.DataReportGraph = False
        if "LuxUVDataView" in history:
            getSecurity.LuxUVDataView = True
        else:
            getSecurity.LuxUVDataView = False
        if "HUserAudit" in history:
            getSecurity.HUserAudit = True
        else:
            getSecurity.HUserAudit = False
        if "HAlarmAudit" in history:
            getSecurity.HAlarmAudit = True
        else:
            getSecurity.HAlarmAudit = False
        if "HSMSAudit" in history:
            getSecurity.HSMSAudit = True
        else:
            getSecurity.HSMSAudit = False
        if "HEquipmentAudit" in history:
            getSecurity.HEquipmentAudit = True
        else:
            getSecurity.HEquipmentAudit = False
        if "HEmailAudit" in history:
            getSecurity.HEmailAudit = True
        else:
            getSecurity.HEmailAudit = False
        
        if "GraphSettings" in tools:
            getSecurity.GraphSettings = True
        else:
            getSecurity.GraphSettings = False
        if "PasswordSettings" in tools:
            getSecurity.PasswordSettings = True
        else:
            getSecurity.PasswordSettings = False
        if "PrintMultipleReports" in tools:
            getSecurity.PrintMultipleReports = True
        else:
            getSecurity.PrintMultipleReports = False
        
        if "AboutUs" in help:
            getSecurity.AboutUs = True
        else:
            getSecurity.AboutUs = False
        if "Help" in help:
            getSecurity.Help = True
        else:
            getSecurity.Help = False
        
        getSecurity.save()
        return redirect("groupsec")

def AssignUserSecurity(request):
    if request.method == "POST":
        getUser = User.objects.get(Username = request.POST['User'])
        getSecurity = GroupSecurity.objects.get(Group=getUser.Group)
        admin = request.POST.getlist('Admin1')
        masterSetting = request.POST.getlist('Master1')
        supervise = request.POST.getlist('Supervise1')
        auditTrails = request.POST.getlist('Audit1')
        history = request.POST.getlist('History1')
        tools = request.POST.getlist('Tool1')
        help = request.POST.getlist('Help1')

        if "UserCreation" in admin:
            getSecurity.UserCreation = True
        else:
            getSecurity.UserCreation = False
        if "GroupSec" in admin:
            getSecurity.GroupSec = True
        else:
            getSecurity.GroupSec = False
        if "UserSec" in admin:
            getSecurity.UserSec = True
        else:
            getSecurity.UserSec = False
        if "DatabaseSetting" in admin:
            getSecurity.DatabaseSetting = True
        else:
            getSecurity.DatabaseSetting = False
        if "SMSsetting" in admin:
            getSecurity.SMSsetting = True
        else:
            getSecurity.SMSsetting = False
        if "EmailSetting" in admin:
            getSecurity.EmailSetting = True
        else:
            getSecurity.EmailSetting = False
        if "MasterPasswdSetting" in admin:
            getSecurity.MasterPasswdSetting = True
        else:
            getSecurity.MasterPasswdSetting = False
        if "GeneralSetting" in admin:
            getSecurity.GeneralSetting = True
        else:
            getSecurity.GeneralSetting = False
        
        if "EquipmentCreation" in masterSetting:
            getSecurity.EquipmentCreation = True
        else:
            getSecurity.EquipmentCreation = False
        if "EquipmentParameter" in masterSetting:
            getSecurity.EquipmentParameter = True
        else:
            getSecurity.EquipmentParameter = False
        if "EquipmentActivation" in masterSetting:
            getSecurity.EquipmentActivation = True
        else:
            getSecurity.EquipmentActivation = False
        if "Template" in masterSetting:
            getSecurity.Template = True
        else:
            getSecurity.Template = False
        if "MobileNumber" in masterSetting:
            getSecurity.MobileNumber = True
        else:
            getSecurity.MobileNumber = False
        if "MasterTemplate" in masterSetting:
            getSecurity.MasterTemplate = True
        else:
            getSecurity.MasterTemplate = False
        if "SyncDataTime" in masterSetting:
            getSecurity.SyncDataTime = True
        else:
            getSecurity.SyncDataTime = False
        if "ResetLuxUV" in masterSetting:
            getSecurity.ResetLuxUV = True
        else:
            getSecurity.ResetLuxUV = False
        if "InputOutputStatus" in masterSetting:
            getSecurity.InputOutputStatus = True
        else:
            getSecurity.InputOutputStatus = False
        
        if "EquipmentList" in supervise:
            getSecurity.EquipmentList = True
        else:
            getSecurity.EquipmentList = False
        if "DataView" in supervise:
            getSecurity.DataView = True
        else:
            getSecurity.DataView = False
        if "LuxUVDataView" in supervise:
            getSecurity.LuxUVDataView = True
        else:
            getSecurity.LuxUVDataView = False
        if "ReportApproval" in supervise:
            getSecurity.ReportApproval = True
        else:
            getSecurity.ReportApproval = False
        if "StatusReports" in supervise:
            getSecurity.StatusReports = True
        else:
            getSecurity.StatusReports = False
        
        if "UserAudit" in auditTrails:
            getSecurity.UserAudit = True
        else:
            getSecurity.UserAudit = False
        if "AlarmAudit" in auditTrails:
            getSecurity.AlarmAudit = True
        else:
            getSecurity.AlarmAudit = False
        if "SMSAudit" in auditTrails:
            getSecurity.SMSAudit = True
        else:
            getSecurity.SMSAudit = False
        if "EquipmentAudit" in auditTrails:
            getSecurity.EquipmentAudit = True
        else:
            getSecurity.EquipmentAudit = False
        if "EmailAudit" in auditTrails:
            getSecurity.EmailAudit = True
        else:
            getSecurity.EmailAudit = False
        
        if "DataReportGraph" in history:
            getSecurity.DataReportGraph = True
        else:
            getSecurity.DataReportGraph = False
        if "LuxUVDataView" in history:
            getSecurity.LuxUVDataView = True
        else:
            getSecurity.LuxUVDataView = False
        if "HUserAudit" in history:
            getSecurity.HUserAudit = True
        else:
            getSecurity.HUserAudit = False
        if "HAlarmAudit" in history:
            getSecurity.HAlarmAudit = True
        else:
            getSecurity.HAlarmAudit = False
        if "HSMSAudit" in history:
            getSecurity.HSMSAudit = True
        else:
            getSecurity.HSMSAudit = False
        if "HEquipmentAudit" in history:
            getSecurity.HEquipmentAudit = True
        else:
            getSecurity.HEquipmentAudit = False
        if "HEmailAudit" in history:
            getSecurity.HEmailAudit = True
        else:
            getSecurity.HEmailAudit = False
        
        if "GraphSettings" in tools:
            getSecurity.GraphSettings = True
        else:
            getSecurity.GraphSettings = False
        if "PasswordSettings" in tools:
            getSecurity.PasswordSettings = True
        else:
            getSecurity.PasswordSettings = False
        if "PrintMultipleReports" in tools:
            getSecurity.PrintMultipleReports = True
        else:
            getSecurity.PrintMultipleReports = False
        
        if "AboutUs" in help:
            getSecurity.AboutUs = True
        else:
            getSecurity.AboutUs = False
        if "Help" in help:
            getSecurity.Help = True
        else:
            getSecurity.Help = False
        
        getSecurity.save()
        return redirect("usersec")


def SMSsettings(request):
    return render(request, "nivdas/sms.html")

def EmailSettings(request):
    return render(request, "nivdas/mail.html")

def MPSetting(request):
    return render(request, "nivdas/master_settings.html")

def GeneralSetting(request):
    return render(request, "nivdas/general-setting.html")


def EquipmentCreation(request):
    return render(request, "nivdas/equip_creation.html")

def EquipmentParameter(request):
    return render(request, "nivdas/eqp_param.html")

def EquipmentActivation(request):
    return render(request, "nivdas/eqp_activ.html")

def MSTemplate(request):
    return render(request, "nivdas/ms-template.html")

def MobileNo(request):
    return render(request, "nivdas/ms-mobile-number.html")

def MasterTemplate(request):
    return render(request, "nivdas/ms-master-template.html")

def SyncDateTime(request):
    return render(request, "nivdas/ms-sync-datetime.html")

def ResetLuxUV(request):
    return render(request, "nivdas/ms-reset-luxuv.html")

def IOStatus(request):
    return render(request, "nivdas/io-status.html")


def DataView(request):
    return render(request, "nivdas/supervise-data-view.html")

def LuxUVDataView(request):
    return render(request, "nivdas/supervise-luxuv-data-view.html")


def AuditUser(request):
    return render(request, "nivdas/audit-user.html")

def AuditAlarm(request):
    return render(request, "nivdas/audit-alarm.html")

def AuditSMS(request):
    return render(request, "nivdas/audit-sms.html")

def AuditEquip(request):
    return render(request, "nivdas/audit-equip.html")

def AuditEmail(request):
    return render(request, "nivdas/audit-email.html")


def HistoryAuditUser(request):
    return render(request, "nivdas/history-user-audit.html")

def HistoryAuditAlarm(request):
    return render(request, "nivdas/history-alarm-audit.html")

def HistoryAuditSMS(request):
    return render(request, "nivdas/history-sms-audit.html")

def HistoryAuditEquip(request):
    return render(request, "nivdas/history-equip-audit.html")

def HistoryAuditEmail(request):
    return render(request, "nivdas/history-email-audit.html")

def HistoryDataView(request):
    return render(request, "nivdas/history-data-view.html")

def HistoryLuxUVDataView(request):
    return render(request, "nivdas/history-luxuv-data-view.html")


def GraphSetting(request):
    return render(request, "nivdas/tu-graph-settings.html")

def PasswordSetting(request):
    return render(request, "nivdas/tu-password-setting.html")

def PrintMultipleReports(request):
    return render(request, "nivdas/tu-print-multiple-report.html")

def AboutUs(request):
    return render(request, "nivdas/aboutus.html")