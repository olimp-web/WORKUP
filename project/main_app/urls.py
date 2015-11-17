from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.landing),
    url(r'^search/', views.search),
    url(r'^profile', views.profile),
    url(r'^profile/(?P<id>\d+)/$', views.profile),
=======
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search),
    url(r'^profile', views.profile, name='profile'),
    url(r'^user/(?P<person_id>[0-9]+)', views.UserController)
>>>>>>> dev
]
