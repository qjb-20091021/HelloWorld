
from django.conf.urls import url, include
from . import view
from django.contrib import admin
from notice.views import index
#admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^notice/', include('notice.notice_urls')),
]