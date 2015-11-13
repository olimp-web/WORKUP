from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Person
# Create your views here.


def search(request):
    return HttpResponse('Search')

# @login_required
def profile(request):
    # id = request.user.user_id
    # return UserController(request, id)
    return HttpResponse('profile ' + request.user.email)


def index(request):
    return HttpResponse('Home')


class PersonDetail(generic.DetailView):
    model=Person
    #template_name = "main_app/person_detail.html"