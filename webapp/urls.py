from django.conf.urls import url
from . import views

app_name = 'webapp'
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^singup/$', views.singup),
    url(r'^config/$', views.config),
    url(r'^schedule/$', views.schedule),
    url(r'^users/$', views.users),
    url(r'^paysheet/$', views.paysheet),
]
