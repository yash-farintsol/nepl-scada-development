from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_member, db_setting, admin_group, supervise_group, operator_group
from .forms import MemberForm, SMSForm, MailForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import json
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
import ast
from django.http import JsonResponse


def home(request):
    # all_members = user_member.objects.values()
    if request.user.is_authenticated:
        all_members = user_member.objects.get(u_name=request.user)
        # print(all_members)
        if all_members.group_name == 'Admin':
            gs = admin_group.objects.values().last()
        if all_members.group_name == 'Supervisor':
            gs = supervise_group.objects.values().last()
        if all_members.group_name == 'Operator':
            gs = operator_group.objects.values().last()
        ap = ast.literal_eval(gs['admin_page'])
        ms = ast.literal_eval(gs['master_page'])
        sp = ast.literal_eval(gs['supervise_page'])
        at = ast.literal_eval(gs['audit_page'])
        hi = ast.literal_eval(gs['history_page'])
        he = ast.literal_eval(gs['help_page'])
        usr = ast.literal_eval(all_members.adpages)
        print(all_members.adpages)
        #{'user_management': True, 'group_security': True}

        return render(request, 'index.html', {'ap': ap, 'ms': ms, 'sp': sp, 'at': at, 'he': he, 'hi': hi, 'usr':usr})  # , {'all': all_members})
    else:
        return redirect('/')


def pswd_change(request):
    if request.method == 'POST' or None:
        username = request.POST['username']
        olspswd = request.POST['oldpaswd']
        pswchdu = request.POST['pswchdu']
        usr = user_member.objects.get(u_name=username)
        u_admin = User.objects.get(username=usr.u_name)
        if olspswd == usr.pswd:
            newpaswd = request.POST['newpaswd']
            cnewpaswd = request.POST['cnewpaswd']
            if newpaswd == cnewpaswd:
                usr.pswd = newpaswd
                usr.pswchdu = pswchdu
                usr.pscdate = datetime.now()
                usr.psedate = usr.pscdate + timedelta(days=int(pswchdu))
                usr.save()
                u_admin.set_password(newpaswd)
                u_admin.save()
                print("password changed successfully")
                return redirect('/login')
    else:
        return render(request, 'pswchange.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usr = user_member.objects.get(u_name=username)
        usr = user_member.objects.get(u_name=username)
        if usr.pscdate >= usr.psedate:
            print("Password change")
            return redirect(pswd_change)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request, 'Error logging in')
            print("messages", messages)
            return redirect('/login')
    else:
        return render(request, 'login.html')


def register(request):
    all_members = user_member.objects.values()
    p = ""
    for all in all_members:
        dayss = all['psedate'] - all['pscdate']
        all['pswchdu'] = dayss.days
        # all.save()
    # print(list(all_members)['u_name'])
    if request.user.is_authenticated:
        if request.method == "POST":
            form = MemberForm(request.POST or None)
            usr = User.objects.get(username=form.data['u_name'])
            print(form.data['u_name'])
            for i in list(all_members):
                if (form.data['u_name'] == i['u_name']):
                    p = "user found"

            if (p == "user found"):
                if form.is_valid():
                    user_member.objects.filter(u_name=form.data["u_name"]).update(u_name=form.data["u_name"],
                                                                                  pswd=form.data["pswd"],
                                                                                  pswchdu=form.data["pswchdu"],
                                                                                  group_name=form.data["group_name"],
                                                                                  dept_name=form.data["dept_name"],
                                                                                  status=form.data["status"])

                    usr.set_password(form.data["pswd"])
                    usr.save()
                    userr = user_member.objects.get(u_name=form.data["u_name"])
                    # user.pscdate =
                    if form.data["pswchdu"] != userr.pswchdu:
                        userr.pscdate = datetime.now()
                        userr.psedate = userr.pscdate + timedelta(days=int(form.data['pswchdu']))
                        userr.save()
                        print("date changed")
            else:
                print("elseeeeee")
                if form.is_valid():
                    print("elseeeeee form valid")
                    u_n = form.data['u_name']
                    u_p = form.data['pswd']
                    user = User.objects.create_user(u_n, None, u_p)
                    f = form.save(commit=False)
                    f.sadmin = False
                    f.pscdate = datetime.now()
                    f.psedate = f.pscdate + form.data['pswd']
                    f.adpages = ""
                    f.save()
        return render(request, 'register.html', {'all': all_members})
    else:
        return render(request, 'login.html')

def user_secur(request):
    all_members = user_member.objects.values()
    if request.user.is_authenticated:
        if request.method == 'POST' or None:
            username = request.POST['user']
            adpg = {}
            if (request.POST.getlist('Admin1', '')):
                for i in request.POST.getlist('Admin1', ''):
                    if i == 'User Creation':
                        adpg.update({'user_management': True})
                    elif i == 'Group Security':
                        adpg.update({'group_security': True})
                    elif i == 'User Security':
                        adpg.update({'user_security': True})
                    elif i == 'Database Settings':
                        adpg.update({'database_settings': True})
                    elif i == 'SMS Settings':
                        adpg.update({'sms_settings': True})
                    elif i == 'Master Password Settings':
                        adpg.update({'master_password_settings': True})
                    elif i == 'Master Password Settings':
                        adpg.update({'mail_settings': True})
            if request.POST.getlist('Audit1', ''):
                for i in request.POST.getlist('Audit1', ''):
                    if i == 'User Audit':
                        adpg.update({'user_audit': True})
                    elif i == 'Alarm Audit':
                        adpg.update({'alarm_audit': True})
                    elif i == 'SMS Audit':
                        adpg.update({'sms_audit': True})
                    elif i == 'Equipment Audit':
                        adpg.update({'equipment_audit': True})
            if request.POST.getlist('Audit1', ''):
                for i in request.POST.getlist('Audit1', ''):
                    if i == 'User Audit':
                        adpg.update({'user_audit': True})
                    elif i == 'Alarm Audit':
                        adpg.update({'alarm_audit': True})
                    elif i == 'SMS Audit':
                        adpg.update({'sms_audit': True})
                    elif i == 'Equipment Audit':
                        adpg.update({'equipment_audit': True})
            if request.POST.getlist('Master1', ''):
                for i in request.POST.getlist('Master1', ''):
                    if i == 'Equipment Creation':
                        adpg.update({'equipment_creation': True})
                    elif i == 'Equipment Parameter':
                        adpg.update({'equipment_parameter': True})
                    elif i == 'Equipment Activation':
                        adpg.update({'equipment_activation': True})
                    elif i == 'Template':
                        adpg.update({'template': True})
                    elif i == 'Mobile Number':
                        adpg.update({'mobile_number': True})
                    elif i == 'Master Template':
                        adpg.update({'master_template': True})
                    elif i == 'Synchronize Date Time':
                        adpg.update({'sync_date_time': True})
                    elif i == 'Reset Lux UV':
                        adpg.update({'reset_lux': True})
                    elif i == 'Input Output Status':
                        adpg.update({'iostatus': True})
            if request.POST.getlist('History1', ''):
                for i in request.POST.getlist('History1', ''):
                    if i == 'Data Report/Graph':
                        adpg.update({'data_report': True})
                    elif i == 'Lux UV Data View':
                        adpg.update({'lux_data_view': True})
            if request.POST.getlist('Help1', ''):
                for i in request.POST.getlist('Help1', ''):
                    if i == 'About Us':
                        adpg.update({'about_us': True})
                    elif i == 'Help':
                        adpg.update({'help': True})
            usr = user_member.objects.get(u_name=username)
            usr.adpages = adpg
            usr.save()

        return render(request, 'user_sec.html', {'all': all_members})
    else:
        return render(request, 'login.html')


def group_secur(request):
    admin_page = {}
    supervise_page = {}
    audit_page = {}
    master_page = {}
    history_page = {}
    help_page = {}

    if request.user.is_authenticated:
        all_members = user_member.objects.get(u_name=request.user)
        # print(all_members)
        if all_members.group_name == 'Admin':
            gs = admin_group.objects.values().last()
        if all_members.group_name == 'Supervisor':
            gs = supervise_group.objects.values().last()
        if all_members.group_name == 'Operator':
            gs = operator_group.objects.values().last()
        print("gssssss", gs)
        ap = ast.literal_eval(gs['admin_page'])
        ms = ast.literal_eval(gs['master_page'])
        sp = ast.literal_eval(gs['supervise_page'])
        at = ast.literal_eval(gs['audit_page'])
        hi = ast.literal_eval(gs['history_page'])
        he = ast.literal_eval(gs['help_page'])

        if request.method == "POST" or None:
            # print(request.POST)

            if request.POST['group'] == 'Admin':
                if request.POST.get('Admin0', '') == 'Admin Page':
                    admin_page = {'user_management': True, 'group_security': True, 'user_security': True,
                                  'mail_settings': True, 'sms_settings': True, 'database_settings': True,
                                  'master_password_settings': True}
                elif (request.POST.getlist('Admin1', '')):
                    for i in request.POST.getlist('Admin1', ''):
                        if i == 'User Creation':
                            admin_page.update({'user_management': True})
                        elif i == 'Group Security':
                            admin_page.update({'group_security': True})
                        elif i == 'User Security':
                            admin_page.update({'user_security': True})
                        elif i == 'Database Settings':
                            admin_page.update({'database_settings': True})
                        elif i == 'SMS Settings':
                            admin_page.update({'sms_settings': True})
                        elif i == 'Master Password Settings':
                            admin_page.update({'master_password_settings': True})
                        elif i == 'Master Password Settings':
                            admin_page.update({'mail_settings': True})
                else:
                    admin_page = {}

                if request.POST.get('Supervise0', '') == 'Supervise Page':
                    supervise_page = {'equipment_list': True, 'data_view': True, 'lux_data_view': True}
                elif (request.POST.getlist('Supervise1', '')):
                    for i in request.POST.getlist('Supervise1', ''):
                        if i == 'Equipment List':
                            supervise_page.update({'equipment_list': True})
                        elif i == 'Data View':
                            supervise_page.update({'data_view': True})
                        elif i == 'Lux UV Data View':
                            supervise_page.update({'lux_data_view': True})
                else:
                    supervise_page = {}

                if request.POST.get('Audit0', '') == 'Audit Trails Page':
                    audit_page = {'user_audit': True, 'alarm_audit': True, 'sms_audit': True, 'equipment_audit': True}
                elif request.POST.getlist('Audit1', ''):
                    for i in request.POST.getlist('Audit1', ''):
                        if i == 'User Audit':
                            audit_page.update({'user_audit': True})
                        elif i == 'Alarm Audit':
                            audit_page.update({'alarm_audit': True})
                        elif i == 'SMS Audit':
                            audit_page.update({'sms_audit': True})
                        elif i == 'Equipment Audit':
                            audit_page.update({'equipment_audit': True})
                else:
                    audit_page = {}

                if request.POST.get('Master0', '') == 'Master Settings Page':
                    master_page = {'equipment_creation': True, 'equipment_parameter': True,
                                   'equipment_activation': True, 'template': True, 'mobile_number': True,
                                   'master_template': True, 'sync_date_time': True, 'reset_lux': True, 'iostatus': True}
                elif request.POST.getlist('Master1', ''):
                    for i in request.POST.getlist('Master1', ''):
                        if i == 'Equipment Creation':
                            master_page.update({'equipment_creation': True})
                        elif i == 'Equipment Parameter':
                            master_page.update({'equipment_parameter': True})
                        elif i == 'Equipment Activation':
                            master_page.update({'equipment_activation': True})
                        elif i == 'Template':
                            master_page.update({'template': True})
                        elif i == 'Mobile Number':
                            master_page.update({'mobile_number': True})
                        elif i == 'Master Template':
                            master_page.update({'master_template': True})
                        elif i == 'Synchronize Date Time':
                            master_page.update({'sync_date_time': True})
                        elif i == 'Reset Lux UV':
                            master_page.update({'reset_lux': True})
                        elif i == 'Input Output Status':
                            master_page.update({'iostatus': True})
                else:
                    master_page = {}

                if request.POST.get('History0', '') == 'History Page':
                    history_page = {'data_report': True, 'lux_data_view': True}
                elif request.POST.getlist('History1', ''):
                    for i in request.POST.getlist('History1', ''):
                        if i == 'Data Report/Graph':
                            history_page.update({'data_report': True})
                        elif i == 'Lux UV Data View':
                            history_page.update({'lux_data_view': True})
                else:
                    history_page = {}

                if request.POST.get('Help0', '') == 'Help Page':
                    help_page = {'about_us': True, 'help': True}
                elif request.POST.getlist('Help1', ''):
                    for i in request.POST.getlist('Help1', ''):
                        if i == 'About Us':
                            help_page.update({'about_us': True})
                        elif i == 'Help':
                            help_page.update({'help': True})
                else:
                    help_page = {}

            obj, created = admin_group.objects.update_or_create(
                admin_page=admin_page, supervise_page=supervise_page, audit_page=audit_page, master_page=master_page,
                history_page=history_page, help_page=help_page)

            if request.POST['group'] == 'Supervisor':
                if request.POST.get('Admin0', '') == 'Admin Page':
                    admin_page = {'user_management': True, 'group_security': True, 'user_security': True,
                                  'mail_settings': True, 'sms_settings': True, 'database_settings': True,
                                  'master_password_settings': True}
                elif (request.POST.getlist('Admin1', '')):
                    for i in request.POST.getlist('Admin1', ''):
                        if i == 'User Creation':
                            admin_page.update({'user_management': True})
                        elif i == 'Group Security':
                            admin_page.update({'group_security': True})
                        elif i == 'User Security':
                            admin_page.update({'user_security': True})
                        elif i == 'Database Settings':
                            admin_page.update({'database_settings': True})
                        elif i == 'SMS Settings':
                            admin_page.update({'sms_settings': True})
                        elif i == 'Master Password Settings':
                            admin_page.update({'master_password_settings': True})
                        elif i == 'Master Password Settings':
                            admin_page.update({'mail_settings': True})
                else:
                    admin_page = {}

                if request.POST.get('Supervise0', '') == 'Supervise Page':
                    supervise_page = {'equipment_list': True, 'data_view': True, 'lux_data_view': True}
                elif (request.POST.getlist('Supervise1', '')):
                    for i in request.POST.getlist('Supervise1', ''):
                        if i == 'Equipment List':
                            supervise_page.update({'equipment_list': True})
                        elif i == 'Data View':
                            supervise_page.update({'data_view': True})
                        elif i == 'Lux UV Data View':
                            supervise_page.update({'lux_data_view': True})
                else:
                    supervise_page = {}

                if request.POST.get('Audit0', '') == 'Audit Trails Page':
                    audit_page = {'user_audit': True, 'alarm_audit': True, 'sms_audit': True, 'equipment_audit': True}
                elif request.POST.getlist('Audit1', ''):
                    for i in request.POST.getlist('Audit1', ''):
                        if i == 'User Audit':
                            audit_page.update({'user_audit': True})
                        elif i == 'Alarm Audit':
                            audit_page.update({'alarm_audit': True})
                        elif i == 'SMS Audit':
                            audit_page.update({'sms_audit': True})
                        elif i == 'Equipment Audit':
                            audit_page.update({'equipment_audit': True})
                else:
                    audit_page = {}

                if request.POST.get('Master0', '') == 'Master Settings Page':
                    master_page = {'equipment_creation': True, 'equipment_parameter': True,
                                   'equipment_activation': True, 'template': True, 'mobile_number': True,
                                   'master_template': True, 'sync_date_time': True, 'reset_lux': True, 'iostatus': True}
                elif request.POST.getlist('Master1', ''):
                    for i in request.POST.getlist('Master1', ''):
                        if i == 'Equipment Creation':
                            master_page.update({'equipment_creation': True})
                        elif i == 'Equipment Parameter':
                            master_page.update({'equipment_parameter': True})
                        elif i == 'Equipment Activation':
                            master_page.update({'equipment_activation': True})
                        elif i == 'Template':
                            master_page.update({'template': True})
                        elif i == 'Mobile Number':
                            master_page.update({'mobile_number': True})
                        elif i == 'Master Template':
                            master_page.update({'master_template': True})
                        elif i == 'Synchronize Date Time':
                            master_page.update({'sync_date_time': True})
                        elif i == 'Reset Lux UV':
                            master_page.update({'reset_lux': True})
                        elif i == 'Input Output Status':
                            master_page.update({'iostatus': True})
                else:
                    master_page = {}

                if request.POST.get('History0', '') == 'History Page':
                    history_page = {'data_report': True, 'lux_data_view': True}
                elif request.POST.getlist('History1', ''):
                    for i in request.POST.getlist('History1', ''):
                        if i == 'Data Report/Graph':
                            history_page.update({'data_report': True})
                        elif i == 'Lux UV Data View':
                            history_page.update({'lux_data_view': True})
                else:
                    history_page = {}

                if request.POST.get('Help0', '') == 'Help Page':
                    help_page = {'about_us': True, 'help': True}
                elif request.POST.getlist('Help1', ''):
                    for i in request.POST.getlist('Help1', ''):
                        if i == 'About Us':
                            help_page.update({'about_us': True})
                        elif i == 'Help':
                            help_page.update({'help': True})
                else:
                    help_page = {}

            obj, created = supervise_group.objects.update_or_create(
                admin_page=admin_page, supervise_page=supervise_page, audit_page=audit_page, master_page=master_page,
                history_page=history_page, help_page=help_page)

            if request.POST['group'] == 'Operator':
                if request.POST.get('Admin0', '') == 'Admin Page':
                    admin_page = {'user_management': True, 'group_security': True, 'user_security': True,
                                  'mail_settings': True, 'sms_settings': True, 'database_settings': True,
                                  'master_password_settings': True}
                elif (request.POST.getlist('Admin1', '')):
                    for i in request.POST.getlist('Admin1', ''):
                        if i == 'User Creation':
                            admin_page.update({'user_management': True})
                        elif i == 'Group Security':
                            admin_page.update({'group_security': True})
                        elif i == 'User Security':
                            admin_page.update({'user_security': True})
                        elif i == 'Database Settings':
                            admin_page.update({'database_settings': True})
                        elif i == 'SMS Settings':
                            admin_page.update({'sms_settings': True})
                        elif i == 'Master Password Settings':
                            admin_page.update({'master_password_settings': True})
                        elif i == 'Master Password Settings':
                            admin_page.update({'mail_settings': True})
                else:
                    admin_page = {}

                if request.POST.get('Supervise0', '') == 'Supervise Page':
                    supervise_page = {'equipment_list': True, 'data_view': True, 'lux_data_view': True}
                elif (request.POST.getlist('Supervise1', '')):
                    for i in request.POST.getlist('Supervise1', ''):
                        if i == 'Equipment List':
                            supervise_page.update({'equipment_list': True})
                        elif i == 'Data View':
                            supervise_page.update({'data_view': True})
                        elif i == 'Lux UV Data View':
                            supervise_page.update({'lux_data_view': True})
                else:
                    supervise_page = {}

                if request.POST.get('Audit0', '') == 'Audit Trails Page':
                    audit_page = {'user_audit': True, 'alarm_audit': True, 'sms_audit': True, 'equipment_audit': True}
                elif request.POST.getlist('Audit1', ''):
                    for i in request.POST.getlist('Audit1', ''):
                        if i == 'User Audit':
                            audit_page.update({'user_audit': True})
                        elif i == 'Alarm Audit':
                            audit_page.update({'alarm_audit': True})
                        elif i == 'SMS Audit':
                            audit_page.update({'sms_audit': True})
                        elif i == 'Equipment Audit':
                            audit_page.update({'equipment_audit': True})
                else:
                    audit_page = {}

                if request.POST.get('Master0', '') == 'Master Settings Page':
                    master_page = {'equipment_creation': True, 'equipment_parameter': True,
                                   'equipment_activation': True, 'template': True, 'mobile_number': True,
                                   'master_template': True, 'sync_date_time': True, 'reset_lux': True, 'iostatus': True}
                elif request.POST.getlist('Master1', ''):
                    for i in request.POST.getlist('Master1', ''):
                        if i == 'Equipment Creation':
                            master_page.update({'equipment_creation': True})
                        elif i == 'Equipment Parameter':
                            master_page.update({'equipment_parameter': True})
                        elif i == 'Equipment Activation':
                            master_page.update({'equipment_activation': True})
                        elif i == 'Template':
                            master_page.update({'template': True})
                        elif i == 'Mobile Number':
                            master_page.update({'mobile_number': True})
                        elif i == 'Master Template':
                            master_page.update({'master_template': True})
                        elif i == 'Synchronize Date Time':
                            master_page.update({'sync_date_time': True})
                        elif i == 'Reset Lux UV':
                            master_page.update({'reset_lux': True})
                        elif i == 'Input Output Status':
                            master_page.update({'iostatus': True})
                else:
                    master_page = {}

                if request.POST.get('History0', '') == 'History Page':
                    history_page = {'data_report': True, 'lux_data_view': True}
                elif request.POST.getlist('History1', ''):
                    for i in request.POST.getlist('History1', ''):
                        if i == 'Data Report/Graph':
                            history_page.update({'data_report': True})
                        elif i == 'Lux UV Data View':
                            history_page.update({'lux_data_view': True})
                else:
                    history_page = {}

                if request.POST.get('Help0', '') == 'Help Page':
                    help_page = {'about_us': True, 'help': True}
                elif request.POST.getlist('Help1', ''):
                    for i in request.POST.getlist('Help1', ''):
                        if i == 'About Us':
                            help_page.update({'about_us': True})
                        elif i == 'Help':
                            help_page.update({'help': True})
                else:
                    help_page = {}

            obj, created = operator_group.objects.update_or_create(
                admin_page=admin_page, supervise_page=supervise_page, audit_page=audit_page, master_page=master_page,
                history_page=history_page, help_page=help_page)

        return render(request, 'group_sec.html',
                      {'ap': ap, 'ms': ms, 'sp': sp, 'at': at, 'he': he, 'hi': hi})  # , {'all': all_members})
    else:
        return render(request, 'login.html')

def Samp(request):
    return render(request, "sample.html")

def AuditUser(request):
    return render(request, "audit-user.html")

def AuditAlarm(request):
    return render(request, "audit-alarm.html")

def AuditSMS(request):
    return render(request, "audit-sms.html")

def AuditEquip(request):
    return render(request, "audit-equip.html")

def AuditEmail(request):
    return render(request, "audit-email.html")

def SMSSetting(request):
    # all_members = user_member.objects.values()
    if request.user.is_authenticated:
        form = SMSForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.sms_status = True
            f.save()

        return render(request, 'sms-setting.html')  # , {'all': all_members})
    else:
        return render(request, 'login.html')

def EmailSetting(request):
    # all_members = user_member.objects.values()
    if request.user.is_authenticated:
        form = MailForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.mail_status = True
            f.save()
        return render(request, 'email-setting.html')  # , {'all': all_members})
    else:
        return render(request, 'login.html')

def DBSetting(request):
    # all_members = user_member.objects.values()
    if request.user.is_authenticated:
        if request.method == "POST" or None:
            db, created = db_setting.objects.get_or_create(
                days=request.POST['days'],
                t1inv=datetime.strptime(request.POST['t1inv'], '%H:%M').time(),
                t2inv=datetime.strptime(request.POST['t2inv'], '%H:%M').time(),
                t3inv=datetime.strptime(request.POST['t3inv'], '%H:%M').time(),
                t4inv=datetime.strptime(request.POST['t4inv'], '%H:%M').time(),
                t5inv=datetime.strptime(request.POST['t5inv'], '%H:%M').time(),
                t1activ=True,
                t2activ=True,
                t3activ=True,
                t4activ=True,
                t5activ=True,
                db_path=request.POST['db_path'],
                bkup_status=request.POST['bkup_status'],
                lastdatabckup=datetime.now(),
            )
            print(request.POST)
        return render(request, 'db-setting.html')  # , {'all': all_members})
    else:
        return render(request, 'login.html')

def MPSetting(request):
    # all_members = user_member.objects.values()
    um_admin = user_member.objects.get(sadmin=True)
    print('um_adminnnnnn', um_admin.u_name)
    u_admin = User.objects.get(username=um_admin.u_name)
    if request.user.is_authenticated:
        if request.method == "POST":
            olspswd = request.POST['oldpaswd']
            if olspswd == um_admin.pswd:
                newpaswd = request.POST['newpaswd']
                cnewpaswd = request.POST['cnewpaswd']
                if newpaswd == cnewpaswd:
                    um_admin.pswd = newpaswd
                    um_admin.save()
                    u_admin.set_password(newpaswd)
                    u_admin.save()
                    print("password changed successfully")
        return render(request, 'master-password-setting.html', {'suser': um_admin})
    else:
        return render(request, 'login.html')

def GeneralSetting(request):
    return render(request, "general-setting.html")

def MSTemplate(request):
    return render(request, "ms-template.html")

def MasterTemplate(request):
    return render(request, "master-template.html")

def SyncDateTime(request):
    return render(request, "sync-datetime.html")

def ResetLuxUV(request):
    return render(request, "reset-luxuv.html")

def IOStatus(request):
    return render(request, "io-status.html")

def GraphSetting(request):
    return render(request, "graph-settings.html")


def equip_create(request):
    all_members = user_member.objects.values()
    return render(request, 'equip_creation.html', {'all': all_members})

def eqp_param(request):
    all_members = user_member.objects.values()
    return render(request, 'eqp_param.html', {'all': all_members})

def eqp_activ(request):
    return render(request, 'eqp_activ.html') #, {'all': all_members, 'alle': all_equip})

def UserUpdateData(request, pk):
    print(pk)
    getann = user_member.objects.get(u_name=pk)
    print(getann)
    data = []
    item = {
        'name': getann.u_name,
        'password': getann.pswd,
        'grp_name': getann.group_name,
        'dep_name': getann.dept_name,
        'status': getann.status,
        'cpassword': getann.pswchdu
    }
    data.append(item)
    return JsonResponse({'data': data})

