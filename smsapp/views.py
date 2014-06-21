from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from coresms.models import *


@login_required
def home(request):
    """
    This function is called when home page(/) is requested.
    A user must be logged in to get its response.

    It automatically redirects user to the login page if they are
    not logged in.
    """
    employee_message_form = EmployeeMessageForm()
    employee_message_form.fields['employees'].queryset = Employee.objects.all()

    department_message_form = DepartmentMessageForm()
    department_message_form.fields[
        'department'].queryset = Department.objects.all()

    group_message_form = GroupMessageForm()
    group_message_form.fields['group'].queryset = Group.objects.all()

    return render(request,
                  'smspage.html',
                  {'employee_message_form': employee_message_form,
                   'department_message_form': department_message_form,
                   'group_message_form': group_message_form})
