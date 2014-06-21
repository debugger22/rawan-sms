from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
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
    employee_message_form.fields['employees'].queryset = Employee.objects.all().order_by('name')

    department_message_form = DepartmentMessageForm()
    department_message_form.fields[
        'department'].queryset = Department.objects.all().order_by('name')

    group_message_form = GroupMessageForm()
    group_message_form.fields['group'].queryset = Group.objects.all().order_by('name')

    return render(request,
                  'smspage.html',
                  {'employee_message_form': employee_message_form,
                   'department_message_form': department_message_form,
                   'group_message_form': group_message_form})


@login_required
def submit_employee_message_form(request):
    if request.method == 'POST':
      # This is the group to which SMS has to be sent
      #try:
      employees_ids = request.POST.get('employees')
      #except DoesNotExist:
      # ToDo: Return to an error page or the same page with
      #       an error message.
      # TODO: Put SMS sending code here
      employee_message = EmployeeMessageForm(request.POST.copy())
      employee_message.save()
      del employee_message
      return HttpResponseRedirect('/')


@login_required
def submit_department_message_form(request):
    if request.method == 'POST':
      # This is the group to which SMS has to be sent
      #try:
      department = Department.objects.get(id=request.POST.get('department'))
      #except DoesNotExist:
      # ToDo: Return to an error page or the same page with
      #       an error message.
      # TODO: Put SMS sending code here
      department_message = DepartmentMessageForm(request.POST.copy())
      department_message.save()
      del department_message
      return HttpResponseRedirect('/')


@login_required
def submit_group_message_form(request):
    if request.method == 'POST':
      # This is the group to which SMS has to be sent
      #try:
      group = Group.objects.get(id=request.POST.get('group'))
      #except DoesNotExist:
      # ToDo: Return to an error page or the same page with
      #       an error message.
      # TODO: Put SMS sending code here
      group_message = GroupMessageForm(request.POST.copy())
      group_message.save()
      del group_message
      return HttpResponseRedirect('/')
