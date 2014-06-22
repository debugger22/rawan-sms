import requests
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from coresms.models import *

def send_sms(mnos, msg):
    fin = open("auth.txt", "r")
    lines = fin.readlines()
    lines = [i.strip() for i in lines]
    payload = {}
    mashape = lines[0].split("::")
    payload[mashape[0]] = mashape[1]
    site2sms_auth = lines[1].split("::")
    uname = site2sms_auth[0]
    pwd = site2sms_auth[1]
    mno_list = "%3B".join(mnos)
    url = "https://site2sms.p.mashape.com/index.php?uid=%s&pwd=%s&phone=%s&msg=%s" % (uname, pwd, mno_list, msg)
    r = requests.get(url, headers=payload)

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
        try:
            employees_ids = request.POST.getlist('employees')
            mno = [Employee.objects.get(id=int(i.encode("utf8"))).mobile.encode("utf8") for i in employees_ids]
            msg = request.POST.get('text')
            send_sms(tuple(set(mno)), msg)
            employee_message = EmployeeMessageForm(request.POST.copy())
            employee_message.save()
            del employee_message
        except DoesNotExist:
            print "Record doesn't exist!"
        return HttpResponseRedirect('/')


@login_required
def submit_department_message_form(request):
    if request.method == 'POST':
        # This is the group to which SMS has to be sent
        try:
            department = Department.objects.get(id=request.POST.get('department'))
            employees = Employee.objects.filter(department=department)
            mno = [i.mobile.encode("utf8") for i in employees]
            msg = request.POST.get('text')
            send_sms(tuple(set(mno)), msg)
            department_message = DepartmentMessageForm(request.POST.copy())
            department_message.save()
            del department_message
        except DoesNotExist:
            print "Department doesn't Exist!"
        return HttpResponseRedirect('/')


@login_required
def submit_group_message_form(request):
    if request.method == 'POST':
        # This is the group to which SMS has to be sent
        try:
            group = Group.objects.get(id=request.POST.get('group'))
            mno = [i.mobile.encode("utf8") for i in group.employees.all()]
            msg = request.POST.get('text')
            send_sms(tuple(set(mno)), msg)
            group_message = GroupMessageForm(request.POST.copy())
            group_message.save()
            del group_message
        except DoesNotExist:
            print "Group doesn't exist!"
        return HttpResponseRedirect('/')
