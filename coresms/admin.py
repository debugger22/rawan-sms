from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import *


class ViewAdminModel(admin.ModelAdmin):

    """
    Custom made change_form template just for viewing purposes.

    """
    change_form_template = 'view_form.html'

    # Remove the delete Admin Action for this Model
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'department')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MessageAdmin(ViewAdminModel):
    list_display = ('text', 'time', 'sent_by')


class EmployeeMessageAdmin(ViewAdminModel):
    list_display = ('text', 'time', 'sent_by')

    def has_add_permission(self, request):
        return False


class DepartmentMessageAdmin(ViewAdminModel):
    list_display = ('text', 'time', 'sent_by', 'department')

    def has_add_permission(self, request):
        return False


class GroupMessageAdmin(ViewAdminModel):
    list_display = ('text', 'time', 'sent_by', 'group')

    def has_add_permission(self, request):
        return False


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(EmployeeMessage, EmployeeMessageAdmin)
admin.site.register(DepartmentMessage, DepartmentMessageAdmin)
admin.site.register(GroupMessage, GroupMessageAdmin)
