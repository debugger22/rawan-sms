from django.contrib import admin
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'department')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'time', 'sent_by')


class EmployeeMessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'time', 'sent_by')


class DepartmentMessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'time', 'sent_by', 'department')


class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'time', 'sent_by', 'group')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(EmployeeMessage, EmployeeMessageAdmin)
admin.site.register(DepartmentMessage, DepartmentMessageAdmin)
admin.site.register(GroupMessage, GroupMessageAdmin)
