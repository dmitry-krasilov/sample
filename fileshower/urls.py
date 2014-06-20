from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import UploadFormView

urlpatterns = patterns(
    url('^$', UploadFormView.as_view(), name='upload_file'),
    url(r'^admin/', include(admin.site.urls)),
)

