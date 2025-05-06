from django.db import models
from problems.models import Problem

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solutions')
    code = models.TextField()
    language = models.CharField(max_length=100)  # Python, C++, Java va hokazo
    explanation = models.TextField(blank=True, null=True)  # ixtiyoriy: yechim haqida tushuntirish

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solution for {self.problem.title}"
