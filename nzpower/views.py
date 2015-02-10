from annoying.decorators import render_to
from nzpower.models import Company

@render_to()
def index(request):
    ctx = {}
    ctx['objs'] = Company.objects.all()
    return ctx

