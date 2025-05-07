from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Problem
from contests.models import Contest
from topics.models import Topic

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    # topics
    topics = problem.topics.all()
    return render(request, 'problem_detail.html', {'problem': problem, 'topics': topics})

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
    return render(request, 'problem_list.html', context)
