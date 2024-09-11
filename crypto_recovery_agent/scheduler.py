## scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from typing import Callable

class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def schedule_task(self, task: Callable, trigger: str = 'interval', interval: int = 60) -> None:
        """
        Schedule a task to be performed regularly.

        :param task: The function to be scheduled.
        :param trigger: The type of trigger for the task. Default is 'interval'.
        :param interval: The interval in seconds at which the task should run. Default is 60 seconds.
        """
        if trigger == 'interval':
            trigger = IntervalTrigger(seconds=interval)
        else:
            raise ValueError("Unsupported trigger type provided.")

        self.scheduler.add_job(task, trigger)

    def start_scheduler(self) -> None:
        """
        Start the scheduler if it's not already running.
        """
        if not self.scheduler.running:
            self.scheduler.start()

    def shutdown_scheduler(self) -> None:
        """
        Shut down the scheduler if it's running.
        """
        if self.scheduler.running:
            self.scheduler.shutdown()
