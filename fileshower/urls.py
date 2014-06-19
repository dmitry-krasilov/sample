from django.conf.urls import patterns, include, url

from views import UploadFormView

urlpatterns = patterns('fileshower.views',
    url('^$', UploadFormView.as_view(), name='upload_file'),
)

