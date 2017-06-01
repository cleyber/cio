from django.conf.urls import url

from . import views

app_name = 'webapp'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^admin/$', views.index_admin, name="admin"),
    url(r'^login/$', views.login, name="login"),
    url(r'^sign_in/$', views.signin, name="signin"),
    url(r'^config/$', views.config, name="config"),
    url(r'^schedule/$', views.schedule, name="schedule"),
    url(r'^users/$', views.users, name="users"),
    url(r'^paysheet/$', views.paysheet, name="paysheet"),
]
