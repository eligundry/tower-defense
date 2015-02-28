from django_cron import CronJobBase, Schedule

from game.models import Game

class TriggerActionJob(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'game.trigger_action_cron'

    def do(self):
        games = Game.objects.filter(is_active=True)

        for game in games.all():
            game.move_enemies()
            game.spawn_enemies()
