from content.models import Section
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def section(request, slug=None):
    context = {
        'section': None,
        'slug': slug,
    }
    return render_to_response('content/section.html',
                              context,
                              context_instance=RequestContext(request))
