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
        return render(request, "nivdas/group_sec.html")
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