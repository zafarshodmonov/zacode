from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Solution
from problems.models import Problem


def solution_list(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    solutions = problem.solutions.all()
    return render(request, 'solution_list.html', {'problem': problem, 'solutions': solutions})


