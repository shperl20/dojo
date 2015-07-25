from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404

from .models import Advisors

# Create your views here.

# this is the main index page
def index(request):
    latest_advisor_list = Advisors.objects.order_by('-advisor_key')[:5]
    context = {'latest_advisor_list': latest_advisor_list}
    return render(request, 'advisor_dash/index.html', context)

# this will render individual advisor pages
def detail(request, advisor_key):
    advisor = get_object_or_404(Advisors, pk=advisor_key)
    return render(request, 'advisor_dash/detail.html', {'advisor': advisor_key})

# this will render advisor results
def results(request, advisor_key):
    response = "You're looking at the results of advisor %s."
    return HttpResponse(response % advisor_key)

# this will render something TBD
def mark(request, advisor_key):
    return HttpResponse("You're marking advisor %s." % advisor_key)
