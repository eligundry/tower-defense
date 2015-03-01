from django_cron import CronJobBase, Schedule
from django.template import Context, loader
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher

from game.models import Game

class TriggerActionJob(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'game.trigger_action_cron'

    def do(self):
        games = Game.objects.filter(is_active=True)

        for game in games.all():
            # Update the enemies
            game.move_enemies()
            # game.spawn_enemies()

            # Send the notification to the users
            # template = loader.load('game/data.json')
            # context = Context({
            #     'game': game,
            #     'monsters': game.gametile_set.exclude(monster__isnull=True),
            #     'towers': game.gametile_set.exclude(tower__isnull=True),
            # })
            #
            # publisher = RedisPublisher(facility='game', id=[game.id])
            # publisher.publish_message(template.render(context))
