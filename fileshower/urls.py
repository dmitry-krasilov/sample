from django.conf.urls import patterns, include, url

urlpatterns = patterns('fileshower.views',
    url('^$', 'upload_file', name = 'upload_file'),
)
