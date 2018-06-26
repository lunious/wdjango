from django.contrib import admin
from .models import *


# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'uname', 'uemail', 'ushou', 'uaddress', 'uphone']


admin.site.register(UserInfo, UserInfoAdmin)
