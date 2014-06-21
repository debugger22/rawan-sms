from __future__ import division

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Department(models.Model):
    """"
    This model holds information of a department.

    Fields
    ======

    name : CharField
        Holds name of the department.

    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    """
    This model holds information of an employee.

    Fields
    ======

    name : CharField
        Holds name of the employee.
    mobile : CharField
        Holds mobile number of the employee
    department : ForeignKey
        Holds department of the employee.

    """
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=13)
    department = models.ForeignKey(Department, related_name='+')

    def __unicode__(self):
        return self.name


class Group(models.Model):
    """
    This model holds information of a custom group.

    Fields
    ======

    name : CharField
        Holds name of the group.
    employees : ManyToManyField
        Holds employee objects.

    """
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, related_name='+', blank=False)

    def __unicode__(self):
        return self.name


class Message(models.Model):
    """
    This is a base class for a message.
    This is an immutable class and hence its fields can not be
    edited once an object has been created.

    Fields
    ======

    text : CharField
        Content of the message
    time : DateTimeField
        Date and time when the message was created.
    sent_by : django.contrib.auth.models.User
        Logged in user at the time of creation of the message.

    """
    text = models.CharField(max_length=140, editable=False)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    sent_by = models.ForeignKey(User, related_name='+', editable=False)

    def __unicode__(self):
        return self.text

class EmployeeMessage(Message):
    employees = models.ManyToManyField(Employee, related_name='+', blank=True)


class DepartmentMessage(Message):
    department = models.ForeignKey(Department, related_name='+')


class GroupMessage(Message):
    group = models.ForeignKey(Group, related_name='+')


class GroupForm(ModelForm):
    class Meta:
        model = Group


class EmployeeMessageForm(ModelForm):
    class Meta:
        model = EmployeeMessage


class DepartmentMessageForm(ModelForm):
    class Meta:
        model = DepartmentMessage


class GroupMessageForm(ModelForm):
    class Meta:
        model = GroupMessage
