from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<entrada_id>\d+)/$', 'blog.views.pub', name='pub'),
    url(r'^(?P<entrada_id>\d+)/comment/$', 'blog.views.comment', name='comment'),
)
