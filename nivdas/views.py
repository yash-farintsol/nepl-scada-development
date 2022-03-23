from django.shortcuts import render, redirect,HttpResponse
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
import ast
from django.http import JsonResponse
from .PdfProcess import html_to_pdf
from django.views.generic import View
from .PlcModbus import *

def LoginPage(request):
    return render(request, "nivdas/login.html")


def IndexPage(request):
    if 'username' in request.session:
        return render(request, "nivdas/dashboard-list.html")
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

def UserSec(request):
    if 'username' in request.session:
        users = User.objects.all()
        return render(request, "nivdas/user_sec.html", {'user': users})
    else:
        return redirect("loginpage")

def DatabaseSettingPage(request):
    if 'username' in request.session:
        return render(request, "nivdas/db-setting.html")
    else:
        return redirect("loginpage")

def SMSsettings(request):
    if 'username' in request.session:
        return render(request, "nivdas/sms.html")
    else:
        return redirect("loginpage")

def EmailSettings(request):
    if 'username' in request.session:
        return render(request, "nivdas/mail.html")
    else:
        return redirect("loginpage")

def MPSetting(request):
    if 'username' in request.session:
        return render(request, "nivdas/master_settings.html")
    else:
        return redirect("loginpage")

def GeneralSetting(request):
    if 'username' in request.session:
        return render(request, "nivdas/general-setting.html")
    else:
        return redirect("loginpage")


def EquipmentCreation(request):
    if 'username' in request.session:
        equipment = Equipment.objects.all()
        return render(request, "nivdas/equip_creation.html", {'equip': equipment})
    else:
        return redirect("loginpage")

def EquipmentParameter(request):
    if 'username' in request.session:
        equipment = Equipment.objects.all()
        return render(request, "nivdas/eqp_param.html", {'equip': equipment})
    else:
        return redirect("loginpage")

def EquipmentActivation(request):
    if 'username' in request.session:
        AllEquip = Equipment.objects.all()
        return render(request, "nivdas/eqp_activ.html",{'eqp':AllEquip})
    else:
        return redirect("loginpage")

def MSTemplate(request):
    if 'username' in request.session:
        return render(request, "nivdas/ms-template.html")
    else:
        return redirect("loginpage")

def MobileNo(request):
    if 'username' in request.session:
        return render(request, "nivdas/ms-mobile-number.html")
    else:
        return redirect("loginpage")

def MasterTemplate(request):
    if 'username' in request.session:
        return render(request, "nivdas/ms-master-template.html")
    else:
        return redirect("loginpage")

def SyncDateTime(request):
    if 'username' in request.session:
        eqps = Equipment.objects.all()
        return render(request, "nivdas/ms-sync-datetime.html",{'eqp':eqps})
    else:
        return redirect("loginpage")

def ResetLuxUV(request):
    if 'username' in request.session:
        return render(request, "nivdas/ms-reset-luxuv.html")
    else:
        return redirect("loginpage")

def IOStatus(request):
    if 'username' in request.session:
        return render(request, "nivdas/io-status.html")
    else:
        return redirect("loginpage")


def DataView(request):
    if 'username' in request.session:
        return render(request, "nivdas/supervise-data-view.html")
    else:
        return redirect("loginpage")

def LuxUVDataView(request):
    if 'username' in request.session:
        return render(request, "nivdas/supervise-luxuv-data-view.html")
    else:
        return redirect("loginpage")


def AuditUser(request):
    if 'username' in request.session:
        return render(request, "nivdas/audit-user.html")
    else:
        return redirect("loginpage")

def AuditAlarm(request):
    if 'username' in request.session:
        return render(request, "nivdas/audit-alarm.html")
    else:
        return redirect("loginpage")

def AuditSMS(request):
    if 'username' in request.session:
        return render(request, "nivdas/audit-sms.html")
    else:
        return redirect("loginpage")

def AuditEquip(request):
    if 'username' in request.session:
        return render(request, "nivdas/audit-equip.html")
    else:
        return redirect("loginpage")

def AuditEmail(request):
    if 'username' in request.session:
        return render(request, "nivdas/audit-email.html")
    else:
        return redirect("loginpage")


def HistoryAuditUser(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-user-audit.html")
    else:
        return redirect("loginpage")

def HistoryAuditAlarm(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-alarm-audit.html")
    else:
        return redirect("loginpage")

def HistoryAuditSMS(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-sms-audit.html")
    else:
        return redirect("loginpage")

def HistoryAuditEquip(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-equip-audit.html")
    else:
        return redirect("loginpage")

def HistoryAuditEmail(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-email-audit.html")
    else:
        return redirect("loginpage")

def HistoryDataView(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-data-view.html")
    else:
        return redirect("loginpage")

def HistoryLuxUVDataView(request):
    if 'username' in request.session:
        return render(request, "nivdas/history-luxuv-data-view.html")
    else:
        return redirect("loginpage")


def GraphSetting(request):
    if 'username' in request.session:
        return render(request, "nivdas/tu-graph-settings.html")
    else:
        return redirect("loginpage")

def PasswordSetting(request):
    if 'username' in request.session:
        return render(request, "nivdas/tu-password-setting.html")
    else:
        return redirect("loginpage")

def PrintMultipleReports(request):
    if 'username' in request.session:
        return render(request, "nivdas/tu-print-multiple-report.html")
    else:
        return redirect("loginpage")

def AboutUs(request):
    if 'username' in request.session:
        return render(request, "nivdas/aboutus.html")
    else:
        return redirect("loginpage")



def Login(request):
    print("HELLO")
    if request.method == "POST":
        
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            message.succes(request, "Username field is required")
            return redirect("loginpage")
        
        if 'password' in request.POST:
            password = request.POST['password']
        else:
            message.succes(request, "Password field is required")
            return redirect("loginpage")
        
        
        usr = User.objects.filter(Username=username)

        if len(usr) > 0:
            if usr[0].status == "Active":
                if usr[0].Password == password:
                    request.session['username'] = usr[0].Username
                    get_user_security = UserSecurity.objects.filter(User=usr[0])
                    get_group_security = GroupSecurity.objects.filter(Group=usr[0].Group)
                    try:
                        if len(get_user_security) > 0:
                            print("GOT USER SECURITY")
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
                            print("GOT GROUP SECURITY")
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
                    except:
                        return redirect("indexpage")
                else:
                    messages.success(request, "Password is Incorrect")
                    return redirect("loginpage")
            else:
                messages.success(request, "Your account is inactive, Please contact the administrator")
                return redirect("loginpage")
        else:
            messages.success(request, "User Doesn't Exist")
            return redirect("loginpage")


def AddUser(request):
    print("FUNCTION CALLED")
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
        'id' : getann.id,
        'name': getann.Username,
        'password': getann.Password,
        'grp_name': getann.Group.GroupName,
        'dep_name': getann.Department,
        'status': getann.status,
        'cpassword': getann.PasswdChangeDuration
    }
    data.append(item)
    return JsonResponse({'data': data})

def UpdateUserData(request):
    if request.method == "POST":
        getuserid = request.POST['id']
        getusr = User.objects.get(id=getuserid)
        getusr.Username = request.POST['usr']
        getgrpname = request.POST['group_name']
        getgrp = Group.objects.get(GroupName = getgrpname)
        getusr.Group = getgrp
        getusr.Department = request.POST['dept_name']
        getusr.status = request.POST['status']
        getusr.Password = request.POST['pswd']
        getusr.PasswdChangeDuration = request.POST['passwdChangeDuration']
        getusr.save()
        print("DATA_UPDATED")
        return redirect("user-management")

def StoreDatabaseSetting(request):
    if request.method == "POST":
        days = request.POST['days']
        time1 = datetime.strptime(request.POST['time1'], '%H:%M').time()
        time2 = datetime.strptime(request.POST['time2'], '%H:%M').time()
        time3 = datetime.strptime(request.POST['time3'], '%H:%M').time()
        time4 = datetime.strptime(request.POST['time4'], '%H:%M').time()
        time5 = datetime.strptime(request.POST['time5'], '%H:%M').time()
        BackupFilePath = request.POST['BackupFilePath']
        AutoBackupStatus = request.POST['AutoBackupStatus']
        HistoryDatabase = request.POST['HistoryDatabase']  


        StoreDBSetting = DatabaseSetting.objects.create(days=days,time1=time1,
        time2=time2,time3=time3,time4=time4,time5=time5,DataBackupPath=BackupFilePath,
        AutoBackupStatus=AutoBackupStatus)

        return redirect("indexpage")

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
    get_sec = UserSecurity.objects.filter(User=GetUser)
    if len(get_sec) > 0:
        get_security = UserSecurity.objects.get(User=GetUser)
    else:
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

def AssignGroupSecurity(request):
    if request.method == "POST":
        getGroup = Group.objects.get(GroupName = request.POST['Group'])
        group_security = GroupSecurity.objects.filter(Group=getGroup)
        if len(group_security) > 0:
            getSecurity = GroupSecurity.objects.get(Group=getGroup)
        else:
            getSecurity = GroupSecurity.objects.create(Group=getGroup)
        print("GetSecurity-->",getSecurity)
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
        user_security = UserSecurity.objects.filter(User=getUser)
        if len(user_security) > 0:
            getSecurity = UserSecurity.objects.get(User=getUser)
        else:
            getSecurity = UserSecurity.objects.create(User=getUser)
        
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

def StoreSmsSetting(request):
    if request.method == "POST":
        interval_time = request.POST['Interval-time']
        port = request.POST['Port-no']
        baud = request.POST['Baud-rate']

        StoreSMSsetting = SMSsetting.objects.create(IntervalTime=interval_time,
        PortNum=port,BaudRate=baud)
        return redirect("indexpage")

def StoreEmailSetting(request):
    if request.method == "POST":
        emailid = request.POST['emailid']
        passwd = request.POST['passwd']
        SMTPserverName = request.POST['smtpservername']
        smtpPort = request.POST['SmtpPort']
        ssl = request.POST['ssl']

        StoreEmail = MailSetting.objects.create(Email=emailid,
        Passwd=passwd,SmtpServerName=SMTPserverName,
        SmtpPort = smtpPort,SSL = ssl
        )

        return redirect("indexpage")

def MasterPasswordSetting(request):
    if request.method == "POST":
        getuser = request.POST['username']
        oldpasswd = request.POST['oldpasswd']
        newpasswd = request.POST['newpasswd']
        confpasswd = request.POST['confpasswd']

        usr = User.objects.get(Username=getuser)
        if usr.Password == oldpasswd:
            if newpasswd == confpasswd:
                usr.Password = confpasswd
                usr.save()
                return redirect("indexpage")
            else:
                print("Password and Confirm password doesn't match")
                return redirect("master-password-setting")
        else:
            print("OLD PASSWORD IS WRONG")
            return redirect("master-password-setting")

def EquipmentList(request):
    if 'username' in request.session:
        return render(request, "nivdas/supervise-equip-list.html")
    else:
        return redirect("loginpage")

def ReportApproval(request):
    if 'username' in request.session:
        return render(request, "nivdas/supervise-report-approval.html")
    else:
        return redirect("loginpage")

def StatusReport(request):
    if 'username' in request.session:
        return render(request, "nivdas/supervise-status-reports.html")
    else:
        return redirect("loginpage")
        # supervise-status-reports


def CreateEquipment(request):
    if request.method == "POST":
        if request.POST['id'] == '':
            Equip = Equipment.objects.create(NumberOfParams = request.POST['param'], NumberOfSensor = request.POST['sensor'])
            print('if')
        else:
            Equip = Equipment.objects.get(id=request.POST['id'])
            print('else')
        EquipmentName = request.POST['eqp_name']
        EquipmentType = request.POST['eqp_type']
        DataLogIntervals = int(request.POST['log_inv'])
        IP1 = request.POST['t1']
        IP2 = request.POST['t2']
        IP3 = request.POST['t3']
        IP4 = request.POST['t4']
        IPaddress = f"{IP1}.{IP2}.{IP3}.{IP4}"
        MachineCode = request.POST['mach_code']
        DepartmentName = request.POST['dep_name']
        Protocol = request.POST['protocol']
        Comments = request.POST['comment']

        Equip.EquipmentName = EquipmentName
        Equip.EquipmentType = EquipmentType
        Equip.IPAddress = IPaddress
        Equip.MachineCode = MachineCode
        Equip.DepartmentName = DepartmentName
        Equip.Protocol = Protocol
        Equip.Comments = Comments
        Equip.DataLogIntervals = DataLogIntervals
        list_checkbox = request.POST.getlist('Dual')
        if "Photo-stability" in list_checkbox:
            Equip.IsPhotoStability = True
        else:
            Equip.IsPhotoStability = False
        if "Dual" in list_checkbox:
            Equip.IsDual = True
        else:
            Equip.IsDual = False
        Equip.save()

        return redirect("equipment-creation")


def EquipParamUpdateData(request, pk):
    print(pk)
    getequip = Equipment.objects.get(EquipmentName=pk)
    print(getequip)
    item = {
        'equip_name' : getequip.EquipmentName,
        'equip_type' : getequip.EquipmentType,
        'param' : getequip.NumberOfParams,
        'sensors' : getequip.NumberOfSensor,
        # 'log_intervals' : getequip.DataLogIntervals,
        # 'ipaddress' : getequip.IPAddress,
        # 'machine_code' : getequip.MachineCode,
        'photostability' : getequip.IsPhotoStability,
        'dual' : getequip.IsDual,
        # 'dep_name' : getequip.DepartmentName,
        # 'protocol' : getequip.Protocol,
        # 'comment' : getequip.Comments
    }
    return JsonResponse({'data': item})

def Graph1(request):
    return render(request, "nivdas/graph.html")

def Graph2(request):
    return render(request, "nivdas/graph2.html")


def StoreTemplate(request):
    if request.method == "POST":
        tempname = request.POST['Temp-name']
        equipname = request.POST['Eqp-name']
        header = request.POST['Header']
        footer = request.POST['Footer']
        address = request.POST['Address']
        logo = request.POST['Logo']

        StoreTemplateConf = MailTemplate.objects.create(TemplateName=tempname,
        EquipmentName=equipname,Header=header,Footer=footer,
        Address=address,Logo=logo)

        return redirect("indexpage")

def samp(request):
    return render(request, 'nivdas/dashboard-grid.html')


def GeneratePdf(request):
    pdf = html_to_pdf('nivdas/samp.html')
    return HttpResponse(pdf, content_type='application/pdf')

def GetData(request):
    output_status()
    print("")
    temp_set()
    print("")
    temp_act_values()
    return redirect("indexpage")

def VerifyUser(request):
    if request.is_ajax():
        print(request.POST)
        user = request.POST['user']
        password = request.POST['pass']
        valid_user = User.objects.filter(Username = user, Password = password)
        if len(valid_user) > 0:
            data = {'valid': "YES"}
            print('------> Yes')
        else:
            data = {'valid': "NO"}
            print('------> No')
        return JsonResponse({'data': data})


def EquipUpdateData(request, pk):
    print(pk)
    equip = Equipment.objects.get(EquipmentName=pk)
    print(equip)
    data = {
        'id' : equip.id,
        'equip_name' : equip.EquipmentName,
        'equip_type': equip.EquipmentType,
        'parameter': equip.NumberOfParams,
        'sensor': equip.NumberOfSensor,
        'data_log': equip.DataLogIntervals,
        'ip_address': equip.IPAddress,
        'machine_code': equip.MachineCode,
        'photo_stability' : equip.IsPhotoStability,
        'dual': equip.IsDual,
        'department': equip.DepartmentName,
        'protocol': equip.Protocol,
        'comment': equip.Comments,
    }
    return JsonResponse({'data': data})

# def UpdateEquipData(request):
#     if request.method == "POST":
#         getid = request.POST['id']
#         getequip = Equipment.objects.get(id=getid)
#         getequip.EquipmentName = request.POST['eqp_name']
#         getequip.EquipmentType = request.POST['eqp_type']
#         # getequip.NumberOfParams = request.POST['param']
#         # getequip.NumberOfSensor = request.POST['sensor']
#         getequip.DataLogIntervals = request.POST['log_inv']
#         IP1 = request.POST['t1']
#         IP2 = request.POST['t2']
#         IP3 = request.POST['t3']
#         IP4 = request.POST['t4']
#         IPaddress = f"{IP1}.{IP2}.{IP3}.{IP4}"
#         getequip.MachineCode = request.POST['usr']
#         getequip.IsPhotoStability = request.POST['dept_name']
#         getequip.IsDual = request.POST['dept_name']
#         getequip.DepartmentName = request.POST['status']
#         getequip.Protocol = request.POST['pswd']
#         getequip.Comments = request.POST['pswd']
#         getequip.save()
#         print("DATA_UPDATED")
#         return redirect("equipment")

def GetPLCDateTime(request):
    if request.method == "POST":
        eid = request.POST['eid']
        print(eid)
        GetEquip = Equipment.objects.get(id=eid)
        print("EQP---->",GetEquip.IPAddress)
        # 
        result = {}
        client = ModbusTcpClient(GetEquip.IPAddress)  # "192.168.1.200"
        connection = client.connect()
        # print("Modbus connection ", connection, '\n')
        values = [400151,400153,400147,400156,400154,400150]
        if connection:
            try:
                for i in values:
                    if i > 400000:
                        if i in [400086, 400087]:
                            ios = client.read_holding_registers(i - 400001, 1, unit=0x01)
                            ios_bin = np.binary_repr(ios.registers[0], width=16)
                            values = list(ios_bin)
                            result[i] = values
                        elif i in [400004, 400025, 400014, 400015, 400016, 400017, 400018, 400019, 400020, 400021, 400022,
                                400023, 400035, 400036, 400037, 400038, 400039, 400040, 400041, 400042, 400043, 400044]:
                            reg = client.read_holding_registers(i - 400001, 1, unit=0x01).registers[0]
                            result[i] = reg / 10
                        else:
                            reg = client.read_holding_registers(i - 400001, 1, unit=0x01).registers[0]
                            result[i] = reg
                    if 0 < i < 99999:
                        alarms = client.read_coils(i - 1, 8, unit=0x01)
                        result[i] = alarms.bits[0]
            except:
                print("SOME ERROR")
                return redirect("synchronize-date-time")
        # 
        print("RESULT----->>>",result)
        # {400151: 18, 400153: 34, 400147: 3}
        hrs = result.get(400151)
        mit = result.get(400153)
        sec = result.get(400147)
        date = result.get(400156)
        month = result.get(400154)
        year = result.get(400150)
        print("HRS | MIT | SEC------>",hrs,mit,sec)
        data = {
            'hrs' : hrs,
            'mit' : mit,
            'sec' : sec,
            'date' : date,
            'month' : month,
            'year' : year
        }
        data.update({'hrs':hrs,'mit':mit,'sec':sec,'date':date,'month' : month,'year':year})
        print(data)
        return JsonResponse({'data': data})