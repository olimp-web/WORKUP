from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def search(request):
    return HttpResponse('Search')

@login_required
def profile(request):
    # id = request.user.user_id
    # return UserController(request, id)
    return HttpResponse('profile')


def index(request):
    return HttpResponse('Home')


def UserController(request, user_id):
    return HttpResponse('User' + user_id)