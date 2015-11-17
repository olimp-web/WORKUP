from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from w_auth.forms import LoginForm
# Create your views here.


def search(request):
    return HttpResponse('Search')

@login_required(login_url=reverse_lazy('w_auth:index'))
def profile(request):
    # id = request.user.user_id
    # return UserController(request, id)
    return HttpResponse('profile ' + request.user.email)


def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:profile'))
    else:
        return render(request, 'index.html', {'login_form': LoginForm()})


def UserController(request, person_id):
    return HttpResponse('User' + person_id)
