from django.shortcuts import render
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def login():
    pass

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:home'))

