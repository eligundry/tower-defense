from django_cron import CronJobBase, Schedule

class TriggerActionJob(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'game.trigger_action_cron'

    def do(self):
        pass
