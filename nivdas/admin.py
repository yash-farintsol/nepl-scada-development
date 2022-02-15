from django.contrib import admin
from .models import user_member, sms_setting, mail_setting, db_setting, admin_group, supervise_group, operator_group

admin.site.register(user_member)
admin.site.register(sms_setting)
admin.site.register(mail_setting)
admin.site.register(db_setting)
admin.site.register(admin_group)
admin.site.register(supervise_group)
admin.site.register(operator_group)