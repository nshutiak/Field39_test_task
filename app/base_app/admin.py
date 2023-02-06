from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Userdata, User

UserAdmin.list_display += ('form_access', )
UserAdmin.list_filter += ('form_access', )
UserAdmin.fieldsets += (('form_access', {'fields': ('form_access', )}), )

admin.site.register(User, UserAdmin)
admin.site.register(Userdata)