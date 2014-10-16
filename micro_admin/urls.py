from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin',

    url(r'^$', 'views.index', name='microadmin_index'),
    url(r'^login/$', 'views.login', name='login'),
    url(r'^sucesslogin/$', 'views.sucesslogin', name='sucesslogin'),
)