from django.conf.urls import url
from django.contrib.auth import logout
from django_skriptD2 import settings
from . import views

app_name = 'oglasi'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'search/$', views.SearchFormView.as_view() , name='search'),

    url(r'register/$', views.UserFormView.as_view(), name='register'),

    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #/oglasi/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /oglasi/oglas/add/
    url(r'oglas/add$', views.OglasCreate.as_view(), name='oglas-add'),

    # /oglasi/oglas/1/
    url(r'oglas/(?P<pk>[0-9]+)/$', views.OglasUpdate.as_view(), name='oglas-update'),

    # /oglasi/oglas/1/delete/
    url(r'oglas/(?P<pk>[0-9]+)/delete/$', views.OglasDelete.as_view(), name='oglas-delete'),

]
