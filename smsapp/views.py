from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,'smspage.html')