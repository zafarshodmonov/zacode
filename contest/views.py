from django.shortcuts import render, get_object_or_404, redirect
from .models import Problem, Contest, Topic

def problem_detail(request, contest_id, problem_index):
    problem = get_object_or_404(Problem, contest__id=contest_id, index=problem_index.upper())
    return render(request, 'problems/problem_detail.html', {'problem': problem})

def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    problems = contest.problems.all().order_by('index')
    return render(request, 'contests/contest_detail.html', {
        'contest': contest,
        'problems': problems,
    })


def contest_list(request):
    contests = Contest.objects.all().order_by('-start_time')
    return render(request, 'contests/contest_list.html', {
        'contests': contests,
    })





