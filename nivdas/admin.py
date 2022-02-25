from django.contrib import admin
from .models import *

admin.site.register(user_member)
admin.site.register(SMSsetting)
admin.site.register(MailSetting)
admin.site.register(DatabaseSetting)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserSecurity)
admin.site.register(GroupSecurity)
admin.site.register(Equipment)
admin.site.register(MailTemplate)