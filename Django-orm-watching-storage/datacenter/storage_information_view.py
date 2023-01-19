from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):

    passcards = Passcard.objects.all()
    visits_without_exits = Visit.objects.filter(entered_at__isnull=False,
                                                leaved_at__isnull=True)
    non_closed_visits = []
    iter = 0

    for visit in visits_without_exits:

        visit_data = {}
        visit_data["who_entered"] = passcards[iter].owner_name
        visit_data["entered_at"] = localtime(visit.entered_at)
        visit_data["duration"] = format_duration(get_duration(visit))
        visit_data["is_strange"] = is_visit_long(visit, 60)
        non_closed_visits.append(visit_data)
        iter += 1

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
