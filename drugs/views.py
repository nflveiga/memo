
from django.http import HttpResponse
from django.template import Context, loader
from drugs.models import Drug
from django.shortcuts import get_object_or_404


def index(request):
    drugs = Drug.objects.all().order_by('name')
    t = loader.get_template('drugs/index.html')
    c = Context({'drugs': drugs, })
    return HttpResponse(t.render(c))

def drugdetail(request, drug_id):
    drug = get_object_or_404(Drug, pk=drug_id)
    t = loader.get_template('drugs/drugdetail.html')
    c = Context({'drug': drug, })
    return HttpResponse(t.render(c))

