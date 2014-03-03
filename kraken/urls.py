from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from api import views

#viewsets define the view behavior.
#router = routers.DefaultRouter()
#router.register(r'clusters', views.ClusterViewSet, 'cluster')

admin.autodiscover()

urlpatterns = patterns('',
    # manage users and permissions
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    # root site
    url(r'^$', 'status.views.home', name='home'),
    # full osd details
    url(r'^osd/(\d+)/$', 'status.views.osd_details', name='osd_details'),
    # kraken API endpoints
    url(r'^api/clusters/health/$', views.health, name="cluster-health"),
    url(r'^api/clusters/status/$', views.status, name="cluster-status"),
    url(r'^api/clusters/overview/$', views.overview, name="cluster-status"),
    url(r'^api/clusters/$', views.clusters, name="clusters"),
    url(r'^api/$', views.api, name="api"),
    # ops endpoints
    url(r'^ops/$', 'ops.views.ops', name='ops'),
)
