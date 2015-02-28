from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('game/index.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))

def new(request):
    template = loader.get_template('game/game.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))

def resume(request, id):
    template = loader.get_template('game/game.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))
