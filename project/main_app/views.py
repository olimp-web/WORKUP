from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy

from w_auth.forms import LoginForm

from main_app.models.person import City, Person
# Create your views here.


def search(request):
    return HttpResponse(request, 'Search')

@login_required(login_url=reverse_lazy('w_auth:index'))
def profile(request):
    account = request.user
    person = Person.objects.get(user=account)
    user_name = person.user_name
    user_surname = person.user_surname
    gender = person.gender
    city = City.objects.select_related().get(id = id)
    c = city.name
    birthday = person.birthday
    return HttpResponse(user_name + ' ' + user_surname + ' ' + c + ' ' + str(birthday) )
    #al = all_c.values("id", "name")
    #qwe = all_c.values
    #all_c1 = all_c.values("id", "name")
    #id_c = City.objects.get(id = id)
    #return HttpResponse('profile ' + all_c)
    #return render_to_response({'articles': City.objects.all()})

def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:profile'))
    else:
        return render(request, 'index.html', {'login_form': LoginForm()})


def UserController(request, person_id):
    return HttpResponse('User' + person_id)
