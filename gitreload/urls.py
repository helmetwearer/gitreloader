from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'gitreload.views.home', name='home'),
)
