
from django.http import HttpResponse
from django.template import Context, loader
from protocols.models import Protocols
from django.shortcuts import get_object_or_404


def index(request):
    protocols = Protocols.objects.all().order_by('name')
    t = loader.get_template('protocols/index.html')
    c = Context({'protocols': protocols, })
    return HttpResponse(t.render(c))

def protocoldetail(request, protocol_id):
    protocol = get_object_or_404(Protocols, pk=protocol_id)
    t = loader.get_template('protocols/protocoldetail.html')
    c = Context({'protocol': protocol, })
    return HttpResponse(t.render(c))

