import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from django.utils.timezone import localtime


if __name__ == '__main__':
    print("Task #1:")
    print('Количество пропусков:', Passcard.objects.count())

    passcards = Passcard.objects.all()
    print("\nTask #2:")
    print(passcards)

    some_passcard = passcards[0]
    print("\nTask #3:")
    print(f"owner_name: {some_passcard.owner_name}")
    print(f"passcode: {some_passcard.passcode}")
    print(f"created_at: {some_passcard.created_at}")
    print(f"is_active: {some_passcard.is_active}")

    active_passcards = [i for i in passcards if i.is_active is True]
    print("\nTask #4:")
    print(f"Всего пропусков: {len(passcards)}")
    print(f"Активных пропусков: {len(active_passcards)}")

    active_passcards = Passcard.objects.filter(is_active=True)
    print("\nTask #5:")
    print(f"Всего пропусков: {len(passcards)}")
    print(f"Активных пропусков: {len(active_passcards)}")

    visits = Visit.objects.all()
    print("\nTask #8:")
    print(visits)

    visits_without_exits = Visit.objects.filter(leaved_at=None)
    print("\nTask #9:")
    print(visits_without_exits)

    print("\nTask #10:")
    for visit in visits_without_exits:

        print("Зашёл в хранилище, время по Москве:")
        print(localtime(visit.entered_at))
        print("\nНаходится в хранилище:")
        print(str(localtime() - localtime(visit.entered_at)).split(".")[0])

    print("\nTask #11:")
    print("Кто сейчас находится в хранилище:")
    for visit in visits_without_exits:
        print(visit.passcard.owner_name)

    print("\nTask #13:")
    some_visits = Visit.objects.filter(passcard=some_passcard)
    print(some_visits)

    print("\nTask #14:")
    visits_more_than_10_minutes = []
    visits_more_than_1000_minutes = []

    for visit in some_visits:
        delta = get_duration(visit).total_seconds()

        if (delta / 60) > 1000:
            visits_more_than_1000_minutes.append(visit)
        elif ((delta / 60) < 1000) & ((delta / 60) > 10):
            visits_more_than_10_minutes.append(visit)

    print(f'''\nВизиты дольше 10 мин (до 1000 мин):\n
            {visits_more_than_10_minutes}''')
    print(f"\nВизиты дольше 1000 мин:\n {visits_more_than_1000_minutes}")
