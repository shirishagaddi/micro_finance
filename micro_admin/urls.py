from django.conf.urls import patterns, include, url

urlpatterns = patterns('micro_admin',

    url(r'^$', 'views.base', name='microadmin_base'),
    url(r'^login/$', 'views.login', name='microadmin_login'),
    url(r'^createbranch/$', 'views.create_branch', name='microadmin_branch'),
)