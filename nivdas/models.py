from django.db import models

class user_member(models.Model):
    objects = models.Manager()
    u_name = models.CharField(max_length=30)
    pswd = models.CharField(max_length=30)
    pswchdu = models.IntegerField()
    group_name = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    sadmin = models.BooleanField()
    ucdate = models.DateTimeField(auto_now_add=True)
    pscdate = models.DateTimeField()
    psedate = models.DateTimeField()
    adpages = models.CharField(max_length=500)
    #logintime = models.DateTimeField(default=0)

class Group(models.Model):
    GroupName = models.CharField(max_length=30)

    def __str__(self):
        return self.GroupName

class GroupSecurity(models.Model):
    Group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True, blank=True)
    UserCreation = models.BooleanField(default=False)
    GroupSec = models.BooleanField(default=False)
    UserSec = models.BooleanField(default=False)
    DatabaseSetting = models.BooleanField(default=False)
    SMSsetting = models.BooleanField(default=False)
    EmailSetting = models.BooleanField(default=False)
    MasterPasswdSetting = models.BooleanField(default=False)
    GeneralSetting = models.BooleanField(default=False)
    EquipmentCreation = models.BooleanField(default=False)
    EquipmentParameter = models.BooleanField(default=False)
    EquipmentActivation = models.BooleanField(default=False)
    Template = models.BooleanField(default=False)
    MobileNumber = models.BooleanField(default=False)
    MasterTemplate = models.BooleanField(default=False)
    SyncDataTime = models.BooleanField(default=False)
    ResetLuxUV = models.BooleanField(default=False)
    InputOutputStatus = models.BooleanField(default=False)
    EquipmentList = models.BooleanField(default=False)
    DataView = models.BooleanField(default=False)
    LuxUVDataView = models.BooleanField(default=False)
    ReportApproval = models.BooleanField(default=False)
    StatusReports = models.BooleanField(default=False)
    UserAudit = models.BooleanField(default=False)
    AlarmAudit = models.BooleanField(default=False)
    SMSAudit = models.BooleanField(default=False)
    EquipmentAudit = models.BooleanField(default=False)
    EmailAudit = models.BooleanField(default=False)
    DataReportGraph = models.BooleanField(default=False)
    LuxUVDataView = models.BooleanField(default=False)
    HUserAudit = models.BooleanField(default=False)
    HAlarmAudit = models.BooleanField(default=False)
    HSMSAudit = models.BooleanField(default=False)
    HEquipmentAudit = models.BooleanField(default=False)
    HEmailAudit = models.BooleanField(default=False)
    GraphSettings = models.BooleanField(default=False)
    PasswordSettings = models.BooleanField(default=False)
    PrintMultipleReports = models.BooleanField(default=False)
    AboutUs = models.BooleanField(default=False)
    Help = models.BooleanField(default=False)

    def __str__(self):
        return self.Group.GroupName




class User(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    PasswdChangeDuration = models.IntegerField()
    Group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True) 
    Department = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    SuperAdmin = models.BooleanField(default=False)
    UserCreatedDate = models.DateTimeField(auto_now_add=True)
    PasswordCreatedDate = models.DateTimeField(auto_now_add=True)
    PasswordExpiryDate = models.DateTimeField(auto_now_add=True)
    Is_Group_Security_Assigned = models.BooleanField(default=False)
    Is_User_Security_Assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.Username

class UserSecurity(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    UserCreation = models.BooleanField(default=False)
    GroupSec = models.BooleanField(default=False)
    UserSec = models.BooleanField(default=False)
    DatabaseSetting = models.BooleanField(default=False)
    SMSsetting = models.BooleanField(default=False)
    EmailSetting = models.BooleanField(default=False)
    MasterPasswdSetting = models.BooleanField(default=False)
    GeneralSetting = models.BooleanField(default=False)
    EquipmentCreation = models.BooleanField(default=False)
    EquipmentParameter = models.BooleanField(default=False)
    EquipmentActivation = models.BooleanField(default=False)
    Template = models.BooleanField(default=False)
    MobileNumber = models.BooleanField(default=False)
    MasterTemplate = models.BooleanField(default=False)
    SyncDataTime = models.BooleanField(default=False)
    ResetLuxUV = models.BooleanField(default=False)
    InputOutputStatus = models.BooleanField(default=False)
    EquipmentList = models.BooleanField(default=False)
    DataView = models.BooleanField(default=False)
    LuxUVDataView = models.BooleanField(default=False)
    ReportApproval = models.BooleanField(default=False)
    StatusReports = models.BooleanField(default=False)
    UserAudit = models.BooleanField(default=False)
    AlarmAudit = models.BooleanField(default=False)
    SMSAudit = models.BooleanField(default=False)
    EquipmentAudit = models.BooleanField(default=False)
    EmailAudit = models.BooleanField(default=False)
    DataReportGraph = models.BooleanField(default=False)
    LuxUVDataView = models.BooleanField(default=False)
    HUserAudit = models.BooleanField(default=False)
    HAlarmAudit = models.BooleanField(default=False)
    HSMSAudit = models.BooleanField(default=False)
    HEquipmentAudit = models.BooleanField(default=False)
    HEmailAudit = models.BooleanField(default=False)
    GraphSettings = models.BooleanField(default=False)
    PasswordSettings = models.BooleanField(default=False)
    PrintMultipleReports = models.BooleanField(default=False)
    AboutUs = models.BooleanField(default=False)
    Help = models.BooleanField(default=False)




class sms_setting(models.Model):
    objects = models.Manager()
    itime = models.IntegerField()
    port_num = models.IntegerField()
    baud_rate = models.IntegerField()
    sms_status = models.BooleanField()

class mail_setting(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=50)
    mpaswd = models.CharField(max_length=50)
    smtp_server = models.CharField(max_length=50)
    smtp_port = models.IntegerField()
    ssl = models.CharField(max_length=50)
    mail_status = models.BooleanField()

class db_setting(models.Model):
    objects = models.Manager()
    days = models.IntegerField()
    t1inv = models.TimeField()
    t1activ = models.BooleanField()
    t2inv = models.TimeField()
    t2activ = models.BooleanField()
    t3inv = models.TimeField()
    t3activ = models.BooleanField()
    t4inv = models.TimeField()
    t4activ = models.BooleanField()
    t5inv = models.TimeField()
    t5activ = models.BooleanField()
    db_path = models.CharField(max_length=50)
    bkup_status = models.CharField(max_length=50)
    lastdatabckup = models.DateTimeField()


class admin_group(models.Model):
    objects = models.Manager()
    group_select = models.CharField(max_length=30)
    admin_page = models.CharField(max_length=500)
    supervise_page = models.CharField(max_length=500)
    audit_page = models.CharField(max_length=500)
    master_page = models.CharField(max_length=500)
    history_page = models.CharField(max_length=500)
    help_page = models.CharField(max_length=500)


class supervise_group(models.Model):
    objects = models.Manager()
    admin_page = models.CharField(max_length=500)
    supervise_page = models.CharField(max_length=500)
    audit_page = models.CharField(max_length=500)
    master_page = models.CharField(max_length=500)
    history_page = models.CharField(max_length=500)
    help_page = models.CharField(max_length=500)


class operator_group(models.Model):
    objects = models.Manager()
    admin_page = models.CharField(max_length=500)
    supervise_page = models.CharField(max_length=500)
    audit_page = models.CharField(max_length=500)
    master_page = models.CharField(max_length=500)
    history_page = models.CharField(max_length=500)
    help_page = models.CharField(max_length=500)
