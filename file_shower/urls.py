from django.conf.urls import patterns, include, url

urlpatterns = patterns('file_shower.views',
    url('^$', 'upload_file', name = 'upload_file'),
)
