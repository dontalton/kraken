from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from cephclient import wrapper

ceph = wrapper.CephWrapper(endpoint=settings.CEPH_BASE_URL)

### Main page
def ops(request):
    return render_to_response('ops.html', locals())

### Root operations
def compact(request):
    response, content = ceph.compact(body='json')

def scrub(request):
    reponse, content = ceph.scrub(body='json')

### MON operations
def mon_remove(request, mon):
    reponse, content = ceph.mon_remove(mon)

### OSD operations
