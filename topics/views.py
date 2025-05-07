from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Topic
from problems.models import Problem


def topic_list(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
    }
    return render(request, 'topic_list.html', context)


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    problems = Problem.objects.filter(topics=topic)
    return render(request, 'topic_detail.html', {'topic': topic, 'problems': problems})
