from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone
from django.template import loader
from django import forms

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

def home(request):
    return render(request, "home.html")

def root(request):
    return redirect('home')
