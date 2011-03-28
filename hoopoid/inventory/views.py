from inventory.models import Hoop
from django.http import HttpResponse
from django.template import Context, loader


def store(request):
    hoop_list = Hoop.objects.all()
    t = loader.get_template('store.html')
    c = Context({
            'hoop_list': hoop_list,
            })
    return HttpResponse(t.render(c))
