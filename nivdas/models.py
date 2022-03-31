from django.db import models
from datetime import datetime
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


class Department(models.Model):
    Department_Name = models.CharField(max_length=100,default="DepartmentName")
    
    def __str__(self):
        return self.Department_Name

class User(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    PasswdChangeDuration = models.IntegerField()
    Group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True) 
    Dep = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=20)
    UserType = models.CharField(max_length=20,default="UserType")
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


class DatabaseSetting(models.Model):
    time1 = models.TimeField()
    time2 = models.TimeField()
    time3 = models.TimeField()
    time4 = models.TimeField()
    time5 = models.TimeField()
    DataBackupPath = models.CharField(max_length=50)
    AutoBackupStatus = models.CharField(max_length=50)
    lastdatabckup = models.DateTimeField(auto_now_add=True)

class SMSsetting(models.Model):
    IntervalTime = models.IntegerField(default=50)
    PortNum = models.IntegerField(default=50)
    BaudRate = models.IntegerField(default=50)
    SmsStatus = models.BooleanField(default=False)

class MailSetting(models.Model):
    Email = models.CharField(max_length=50)
    Passwd = models.CharField(max_length=50)
    SmtpServerName = models.CharField(max_length=50)
    SmtpPort = models.IntegerField()
    SSL = models.CharField(max_length=50)
    Mail_Status = models.BooleanField(default=False)

class Equipment(models.Model):
    EquipmentName = models.CharField(max_length=50)
    EquipmentType = models.CharField(max_length=50)
    NumberOfParams = models.IntegerField(default=0)
    NumberOfSensor = models.IntegerField(default=0)
    DataLogIntervals = models.IntegerField(default=0)
    IPAddress = models.CharField(max_length=50)
    MachineCode = models.CharField(max_length=50)
    IsPhotoStability = models.BooleanField(default=False)
    IsDual = models.BooleanField(default=False)
    DepartmentName = models.CharField(max_length=50,default="Department")
    Protocol = models.CharField(max_length=50,default="PROTOCOL")
    Comments = models.CharField(max_length=200)
    EquipmentActivationStation = models.CharField(max_length=200,default="Inactive")

class MailTemplate(models.Model):
    TemplateName = models.CharField(max_length=200)
    EquipmentName = models.CharField(max_length=200)
    Header = models.CharField(max_length=500)
    Footer = models.CharField(max_length=500)
    Address = models.TextField(default="Address")
    Logo = models.FileField(upload_to="template-logo/",default="no-logo.png")
    
class UserAudit(models.Model):
    User =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Date = models.DateField(default=datetime.now())
    Time = models.TimeField(default=datetime.now().time())
    Comment = models.TextField()
    