from django.contrib import admin

from .models import Permission,fhirip
admin.site.register(Permission)
admin.site.register(fhirip)

from .models import UserLoginRecord

@admin.register(UserLoginRecord)
class UserLoginRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'ip_address', 'user_agent')
    search_fields = ('user__username', 'ip_address', 'user_agent')
    list_filter = ('login_time',)