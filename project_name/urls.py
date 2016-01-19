from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import Http404
from django.views.generic import TemplateView

from inventory.urls import inventory_urlpatterns

from project_name.settings import MEDIA_ROOT, MEDIA_URL

admin.autodiscover()

urlpatterns = patterns('',
    # Admin panel and documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += inventory_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)