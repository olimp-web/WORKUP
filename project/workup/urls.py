from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^adm/', include(admin.site.urls)),
    url(r'^auth/', include('w_auth.urls', namespace='w_auth')),
    url(r'^', include('main_app.urls', namespace='main')),
]
