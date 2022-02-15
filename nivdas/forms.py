from django import forms
from .models import user_member, sms_setting, mail_setting


class MemberForm(forms.ModelForm):
    class Meta:
        model = user_member
        fields = ['u_name', 'pswd', 'pswchdu', 'group_name', 'dept_name', 'status']


class SMSForm(forms.ModelForm):
    class Meta:
        model = sms_setting
        fields = ['itime', 'port_num', 'baud_rate']

class MailForm(forms.ModelForm):
    class Meta:
        model = mail_setting
        fields = ['email', 'mpaswd', 'smtp_server', 'smtp_port', 'ssl', 'mail_status']

