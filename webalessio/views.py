import json

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from webalessio.models import User

def index_json(request):
    return HttpResponse(
        json.dumps(
            { user.id:[user.email, user.suspend_until, user.present] for user in User.objects.all() }))

def index(request):
    return render(request, 'webalessio/daylist.html', {
            'users': User.objects.all(),
        })

def set_presence(request, user_id):
    u = User.objects.get(id=user_id)
    u.present = request.POST.get('present', False)
    if request.POST.get('suspend_until'):
        u.suspend_until = request.POST['suspend_until']
    else:
        u.suspend_until = None
    if request.POST.get('suspend_from'):
        u.suspend_from = request.POST['suspend_from']
    else:
        u.suspend_from = None
    u.save()
    return HttpResponseRedirect(reverse('index'))
