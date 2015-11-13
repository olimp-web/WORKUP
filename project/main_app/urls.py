from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^search', views.search),
    url(r'^profile', views.profile, name='profile'),
    url(r'^user/(?P<pk>[0-9]+)', views.PersonDetail.as_view())
]
