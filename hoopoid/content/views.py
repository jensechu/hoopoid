from content.models import Section
from django.http import HttpResponse

def section(request, slug=None):
    return HttpResponse(slug or "None")
