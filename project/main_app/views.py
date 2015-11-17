from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main_app.models.person import City, Person

# Create your views here.
def search(request):

    return HttpResponse(request, 'Search')

def profile(request, id = 2):
    person = Person.objects.get(id = id)
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



def landing(request):
    return HttpResponse(request, 'Home')
