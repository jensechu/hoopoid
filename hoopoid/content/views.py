from content.models import Section
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

def section(request, slug=None):
    context = {
        'section': None,
        'slug': slug,
        'all_sections': Section.objects.all(),
    }

    try:
        context["section"] = Section.objects.get(slug=slug)
    except Section.DoesNotExist:
        if slug is None:
            context["section"] = Section.objects.get(default=True)
        else:
            raise Http404("No Section with this slug was found.")

    return render_to_response('content/section.html',
                              context,
                              context_instance=RequestContext(request))
