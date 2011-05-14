from inventory.models import Hoop
from content.models import Section
from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response

def store(request):
    context = {
        'hoop_list': Hoop.objects.all(),
        'all_sections': Section.objects.all(),
    }
    return render_to_response('inventory/store.html',
                              context,
                              context_instance=RequestContext(request))


    # t = loader.get_template('store.html')
    # c = RequestContext(request, {
    #         'hoop_list': hoop_list,
    #         })
    # return HttpResponse(t.render(c))

