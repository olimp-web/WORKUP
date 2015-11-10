from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing),
    url(r'^search/', views.search),
    url(r'^profile', views.profile),
]
