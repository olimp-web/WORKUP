from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def search(request):
    return HttpResponse(request, 'Search')

def profile(request):
    return HttpResponse(request, 'UserProfile')

def landing(request):
    return HttpResponse(request, 'Home')