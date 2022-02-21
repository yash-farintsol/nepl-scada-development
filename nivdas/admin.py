from django.contrib import admin
from .models import user_member, SMSsetting, MailSetting, db_setting, admin_group, supervise_group, operator_group,User,Group,UserSecurity,GroupSecurity,DatabaseSetting

admin.site.register(user_member)
admin.site.register(SMSsetting)
admin.site.register(MailSetting)
admin.site.register(DatabaseSetting)
admin.site.register(admin_group)
admin.site.register(supervise_group)
admin.site.register(operator_group)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserSecurity)
admin.site.register(GroupSecurity)