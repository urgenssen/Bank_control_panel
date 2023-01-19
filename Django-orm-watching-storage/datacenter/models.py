from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):

    if visit.leaved_at is None:
        time_in_storage = localtime() - localtime(visit.entered_at)
    else:
        time_in_storage = localtime(visit.leaved_at) - \
             localtime(visit.entered_at)

    return time_in_storage


def format_duration(duration):

    total_seconds = duration.total_seconds()
    days = int(total_seconds // (24 * 3600))
    hours = int((total_seconds - days * 24 * 3600) // 3600)
    minutes = int((total_seconds - days * 24 * 3600 - hours * 3600) // 60)
    seconds = int(total_seconds - days * 24 * 3600
                  - hours * 3600 - minutes * 60)

    total_duration = str(days) + " day(s), " + str(hours).zfill(2) + \
        ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

    return total_duration


def is_visit_long(visit, minutes=60):

    if (get_duration(visit).total_seconds() / 60) > minutes:
        return True
    else:
        return False
