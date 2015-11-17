from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search),
    url(r'^profile', views.profile, name='profile'),
    url(r'^user/(?P<person_id>[0-9]+)', views.UserController)
]
