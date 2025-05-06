from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from contests.models import Contest

def home(request):
    latest_contest = Contest.objects.order_by('-created_at').first()
    return render(request, 'home.html', {'latest_contest': latest_contest})

def base(request):
    return render(request, 'base.html')
