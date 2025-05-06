from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from .models import Contest

def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    problems = contest.problems.all().order_by('index')
    dur_time = contest.end_time - contest.start_time
    return render(request, 'contests/contest_detail.html', {
        'contest': contest,
        'problems': problems,
        'dur_time': str(dur_time),
        'problems_count': contest.problems_count,
    })

def contest_list(request):
    contests = Contest.objects.all().order_by('-start_time')
    return render(request, 'contests/contest_list.html', {
        'contests': contests,
    })
