from django.http import HttpResponse
from django.template import RequestContext, loader

from game.models import Game

def index(request):
    template = loader.get_template('game/index.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))

def new(request):
    game = Game.objects.create_game(10, 10)
    game.save()
    game.add_tiles()

    template = loader.get_template('game/game.html')
    context = RequestContext(request, {
        'game': game,
    })

    return HttpResponse(template.render(context))

def resume(request, id):
    game = Game.objects.get(pk=id)
    active_game_tiles = game.gametile_set.filter(monster__in=range(0, 15))

    template = loader.get_template('game/game.html')
    context = RequestContext(request, {
        'game': game,
        'game_tiles': active_game_tiles,
    })

    return HttpResponse(template.render(context))
