from django.shortcuts import render
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def login(request):
    if not request.POST:
        return render(request, "test_auth_form.html")

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:home'))

