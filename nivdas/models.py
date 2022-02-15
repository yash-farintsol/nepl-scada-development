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
