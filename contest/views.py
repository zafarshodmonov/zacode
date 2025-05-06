from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Problem, Contest, Topic, Solution

def home(request):
    latest_contest = Contest.objects.order_by('-created_at').first()
    return render(request, 'home.html', {'latest_contest': latest_contest})


def problem_detail(request, contest_id, problem_index):
    problem = get_object_or_404(Problem, contest__id=contest_id, index=problem_index.upper())
    return render(request, 'problems/problem_detail.html', {'problem': problem})

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

def base(request):
    return render(request, 'base.html')

def problem_list(request):
    query = request.GET.get('q', '')
    topic_id = request.GET.get('topic', '')

    problems = Problem.objects.all()

    if query:
        problems = problems.filter(
            Q(title__icontains=query) | Q(statement__icontains=query)
        )

    if topic_id:
        problems = problems.filter(topics__id=topic_id)

    topics = Topic.objects.all()

    context = {
        'problems': problems.order_by('contest__start_time', 'index'),
        'query': query,
        'topics': topics,
        'selected_topic_id': topic_id,
    }
    return render(request, 'problems/problem_list.html', context)


def topic_list(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
    }
    return render(request, 'topics/topic_list.html', context)


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    problems = Problem.objects.filter(topics=topic)
    return render(request, 'topics/topic_detail.html', {'topic': topic, 'problems': problems})

def solution_list(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    solutions = problem.solutions.all()
    return render(request, 'solution_list.html', {'problem': problem, 'solutions': solutions})






