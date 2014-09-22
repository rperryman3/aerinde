from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'presentation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^quests/', 'aerinde.views.quests', name='quests'),
    url(r'^$', 'aerinde.views.index', name='index'),

    url(r'^setupa/(?P<userid>\d+)/$', 'aerinde.views.setupa', name='setupa'),
    url(r'^setupb/(?P<userid>\d+)/$', 'aerinde.views.setupb', name='setupb'),

    #url(r'^register/$', 'aerinde.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


    url(r'^admin/', include(admin.site.urls)),
)
