import datetime

from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone

import datetime

@periodic_task(run_every=crontab(day_of_week='*/1'))
def delete_old_files():

    files = UserFile.objects.all()

    # Iterate through them
    for file in files:

        # If the expiration date is bigger than now delete it
        if file.expiration_date < timezone.now():
            file.delete()
            # log deletion
    return f"completed deleting foos at {timezone.now()}"

@periodic_task(run_every=crontab(day_of_week='*/1'))
def update_countdown():

    files = UserFile.objects.all()

    # Iterate through them
    for file in files:
        file.countdown = abs((self.object.expiration_date-
                                    datetime.datetime.utcnow()).days)
